#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import time             # ウェイト用
import argparse         # コマンドライン引数用
import smbus            # I2C制御用
import RPi.GPIO as GPIO # GPIO制御用


#RPi-GP10用インターフェースの初期設定(※下記設定は変更しないでください)
def init_GP10():   
    GPIO.setmode(GPIO.BCM)                              # GPIO番号で指定
    GPIO.setup(27, GPIO.OUT, initial=GPIO.HIGH )        # RPi-GP10絶縁回路用電源ON
    time.sleep(0.5)                                     # 電源安定待ち
    GPIO.setup(STB, GPIO.OUT, initial=GPIO.LOW )        # STB端子出力設定 HIGH (オープンコレクタ)
    GPIO.setup(TRG, GPIO.IN, pull_up_down=GPIO.PUD_OFF) # TRG端子入力設定

    try:
        i2c.write_byte_data(i2c_adrs, 0x06, 0x00)           # 出力端子(ポート0)方向設定 出力
        i2c.write_byte_data(i2c_adrs, 0x04, 0x00)           # 出力端子(ポート0)極性設定 反転なし
        i2c.write_byte_data(i2c_adrs, 0x07, 0xFF)           # 入力端子(ポート1)方向設定 入力
        i2c.write_byte_data(i2c_adrs, 0x05, 0xFF)           # 入力端子(ポート1)極性設定 反転あり
        time.sleep(0.1)                                       
    except:
        print("RPi-GP10の初期化に失敗しました")
        GPIO.output(27,False)                           # RPi-GP10絶縁電源OFF
        GPIO.cleanup()
        sys.exit()




if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                prog='sampleGp10.py',                       #プログラムファイル名
                usage='実行すると入力端子の反転データを表示します', #使用方法
                description='引数を指定することでデータ出力・Trigger・Strobe機能が使用できます',
                epilog=     '--------------------------------------------------------------------------',
                add_help=True,
                )
    #引数
    parser.add_argument('-o', '--output', metavar='[Output]', nargs=1, help='出力反転データを指定 例)-o 0xAB')
    parser.add_argument('-t', '--trg', metavar='[Triger]', nargs=1, help='Triggerを検出すると指定反転データを出力(検出するまで無限ループ) 例)-o 0xCD')
    parser.add_argument('-s', '--stb', metavar='[Strobe]', nargs=1, help='指定反転データが入力されているとStrobeからLow出力 例)-s 0xEF')
    args = parser.parse_args()  #引数確認

    # 初期値設定
    try:
        i2c  = smbus.SMBus(1)       # RPi-GP10はI2C1を使用
    except:
        print("I2Cの設定を確認してください")
        sys.exit()
    
    i2c_adrs = 0x20             # TCA9535 I2Cアドレス 0x20 (RA1～RA6)
    STB  = 14                   # STB出力 GPIO14(JP7:Default) / GPIO12(JP8)
    TRG  = 15                   # TRG入力 GPIO15(JP5:Default) / GPIO13(JP6)

    # RPi-GP10初期化
    init_GP10()         

    # 出力端子制御(引数がある場合)
    if args.output:
        outputData = int(args.output[0], 0)
        try:
            i2c.write_byte_data(i2c_adrs, 0x02, outputData) # 出力端子反転データ書き込み
            print("0x%02X を出力しました" % outputData)        
            time.sleep(0.5)
        except:
            print("信号の出力に失敗しました")        
            GPIO.output(27,False)   # RPi-GP10絶縁回路用電源OFF
            GPIO.cleanup()
            sys.exit()


    # トリガー監視(引数がある場合)
    if args.trg:
        outputData = int(args.trg[0], 0)
        GPIO.add_event_detect(TRG, GPIO.FALLING)

        while True:
            if GPIO.event_detected(TRG):
                print("Trigger!!!")        
                try:
                    i2c.write_byte_data(i2c_adrs, 0x02, outputData) # 出力端子反転データ書き込み
                    print("0x%02X を出力しました" % outputData)        
                    time.sleep(0.5)
                    break
                except:
                    print("信号の出力に失敗しました")        
                    GPIO.output(27,False)   # RPi-GP10絶縁回路用電源OFF
                    GPIO.cleanup()
                    sys.exit()


    # 入力端子の確認
    try:
        inputData = i2c.read_byte_data(i2c_adrs, 0x01)  # 入力端子反転データ読み込み
        print("入力信号: 0x%02X" % inputData)        
    except:
        print("入力信号の検知に失敗しました")        


    # ストローブ出力(引数がある場合)
    if args.stb:
        stbData = int(args.stb[0], 0)

        if inputData == stbData:
            print("Strobe!!!")        
            GPIO.output(STB, True)  # STBをLOWに設定

    GPIO.output(27, False)   # RPi-GP10の絶縁回路用電源OFF
    GPIO.cleanup()
    sys.exit()

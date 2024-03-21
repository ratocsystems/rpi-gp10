# Raspberry Pi OSの設定

Rapberry Pi用のOSである Raspberry Pi OS(Rasbian)の設定について説明します。  
Raspberry Pi本体は'Raspberry Pi3 ModelB'、
Raspberry Pi Imagerは、'Raspberry Pi Imager 1.6.2'、
OSは'Raspberry Pi OS Version 2021-03-04'で説明します。
※2020年5月に名称が「Rasbian」から「Raspberry Pi OS」に変更されました。

## Raspberry Pi OSのインストール  
<a name="osInstallation"></a>

###	1. Class10のmicroSD(8～32G)を用意します。

*64GB以上のSDカードの場合、exFATでフォーマットされます。
Raspberry Pi OSはexFATに対応していませんので、別のツールを使ってFAT16またはFAT32でフォーマットする必要があります。*

### 2. Raspberry財団公式ホームページ( https://raspberrypi.org/software/ )でRaspberry Pi Imager をダウンロードしてインストールします。

2-1. ダウンロードしたファイルをダブルクリックします。

![01](./img/imager-00.png)  

2-2. [Install] をクリックします。

![02](./img/imager-01.png)  

2-3. 終了画面で[Finish]をクリックします。

![03](./img/imager-02.png)  

### 3. Raspberry Pi Imager を使って Raspberry Pi OS のSDカードを作成します。

3-1. Raspberry Pi Imagerが起動すると以下の画面が表示されます。

   ![01](./img/osInstall-01.png)  

3-2. [CHOOSE OS]をクリックして[Raspberry Pi OS (32-bit)]を選択します。

   ![02](./img/osInstall-02.png) 

3-3. [CHOOSE SD CARD]をクリックして、書き込み先のデバイス（SD Card）を選択します。
 
  ![03](./img/osInstall-03.png) 

3-4. [WRITE] をクリックします。

  ![04](./img/osInstall-04.png) 

3-5. 確認ダイアログ画面で [YES]を選択して、SD Cardへの書き込みを開始します。

  ![05](./img/osInstall-05.png) 

3-6. 途中、書き込みの進捗状況が表示されます。

  ![06](./img/osInstall-07.png) 

3-7. 書き込みが終わると、以下の完了画面が表示されます。
　　[CONTINUE] をクリックして、microSDカードを取り外します。

  ![07](./img/osInstall-08.png) 

### 4. OSの起動と日本語モードの設定

4-1. microSDカードをRaspberry Pi基板に接続し起動します。  

  ![08](./img/osInstall-09.png) 

4-2. [Preferense]-[Raspberry Pi Configuration]をクリックします。

  ![09](./img/piConfig-01.jpg) 

4-3. [Localisation] をクリックします。

  ![10](./img/piConfig-02.jpg) 

4-4. [Set Locale...] をクリックします。

  ![11](./img/piConfig-03.jpg) 

4-5. Language 項目で[ja(Japanese)] を
   Character Set項目で[EUC-JP]か、[UTF-8 ]を選択します。
   最後に[OK]クリックします。

  ![12](./img/piConfig-04.jpg) 

4-6. [Raspberry Pi Configuration]の画面で[OK]をクリックすると、
　[Reboot needed] の再起動の確認が表示されるので[Yes]をクリックします。

4-7. 再起動後、Raspberry Pi OSの日本語モードの画面が表示されます。

4-8. [設定]-[Raspberry Pi の設定]をクリックします。

   ![01](./img/i2cSetting-01.jpg)  

4-9. [ローカライゼーション] をクリックします。

  必要に応じて、タイムゾーンの設定、キーボードの設定、無線LANの国設定 等の設定を行います。

引き続き、I2Cの設定を行います。

## I2Cの有効設定  

### [Raspberry Pi の設定]の[インターフェース]で"I2C"を有効にします。

   ![02](./img/i2cSetting-02.jpg)  

設定を反映させるため、OSを再起動すれば、Raspberry Pi OS のインストールと設定は完了です。
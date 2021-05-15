# ESP32 + MicroPythonサンプル集

インターフェース誌に連載している「逆引きMicroPython」プログラム集のソースコードです。

- スイッチやボリューム，ロータリ・エンコーダによる入力検出([Interface 2021年5月号](https://interface.cqpub.co.jp/magazine/202105/))
   - フォルダ：[NO2_SW_VR](https://github.com/ESPuPy/ESP32-MicroPython-Samples/tree/master/NO2_SW_VR)

|ファイル名|内容|備考|
|-|-|-|
|[list1.py](NO2_SW_VR/list1.py)|SWを押した時LED点灯|ポーリングによる実装|
|[list2.py](NO2_SW_VR/list2.py)|SWを押すとLEDの点灯・消灯が切り替わる|割り込みによる実装|
|[list3.py](NO2_SW_VR/list3.py)|ADCサンプル|
|[list5.py](NO2_SW_VR/list4.py)|ロータリエンコーダサンプル|下記ドライバが必要です|
|[encoder.py](NO2_SW_VR/encoder.py)|ロータリエンコーダドライバ|ポーリングによる実装|

- センサ入力(Interface 2021年6月号)
- PWM出力(Interface 2021年7月号)([Interface 2021年7月号](https://interface.cqpub.co.jp/magazine/202107/))
   - フォルダ：[NO4_PWM](https://github.com/ESPuPy/ESP32-MicroPython-Samples/tree/master/NO4_PWM)
|ファイル名|内容|備考|
|-|-|-|
|[list1.py](NO4_PWM/list1.py)|PWMによるLEDの輝度制御||
|[list2.py](NO4_PWM/list2.py)|PWMによるLEDの輝度制御（VRに連動）|AD変換でVRの位置を判定|
|[list3.py](NO4_PWM/list3.py)|PWMによるサーボ制御(VRに連動)|AD変換でVRの位置を判定|
|[list4.py](NO4_PWM/list4.py)|PWMによるメロディ再生||
|[list5.py](NO4_PWM/list5.py)|ロータリエンコーダに連動して音程を変える|下記ドライバが必要です|
|[encoder.py](NO4_PWM/encoder.py)|ロータリエンコーダドライバ|ポーリングによる実装|

- ディスプレイ出力(Interface 2021年8月号)
- シリアル通信(Interface 2021年9月号)
- ファイル操作(Interface 2021年10月号)
- クラウド通信/サーバ機能(Interface 2021年11月号)
- スリープ機能(Interface 2021年12月号)
- タイマ機能(Interface 2022年1月号)
- コード改善とメモリ管理(Interface 2022年2月号)



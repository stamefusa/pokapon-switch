## 概要
Nintendo SwitchのJoyConを使ってサーボを動かすのに使ったコードです。

* pokapon.py  
メインのコードです。下記のサンプルを組み合わせています。
* read_com.py  
pygameを使ってJoyCon（または単なるゲームパッド）の入力を取得するコードです。  
下記のブログエントリにあるコードをそのまま使っています。thanks.  
https://divide-et-impera.org/archives/1398
* servo.py  
pigpioを使ってサーボを制御させるサンプルです。

# 授業の内容をそのままあげてるよ
更新は私が飽きるまではやるとおもうよ
仮想環境は載せないからそこは自分で作成してね

## 仮想環境の作り方
 - Python ver 3.9.7がインストールされていることが前提
 - またflaskはflask==2.3.3を使用する(下の手順で解決可能)
```
C:\Users\<User名>\AppData\Local\Programs\Python\Python39\python.exe -m venv <ファイル名>
```
これを作成したい階層で実行することで作成可能

## pip installについて
requirements.txtをvenv内に配置し、仮想環境内で
```
pip install -r requirements.txt
```
を実行すれば現時点でのpip installしないといけないものはインストールされる
pip listを使って確認してね

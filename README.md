# etude_gae

GCP-GAEを用いて簡単なTodo-listを作成する

## 手順

1. Cloud SDKを有効化: ターミナル、端末等のShell側からGCPのリソースを管理できるSDK（Software Development Kit）です。
2. Python実行環境を作成する 

### 1. Cloud SDKを有効化

#### 1-1. Google Cloud SDKをダウンロード  

[Cloud SDKのインストール](https://cloud.google.com/sdk/docs/install?hl=JA#installation_instructions) から自分のOS、バージョンに合わせたパッケージをダウンロードする。
(保存場所を指定しなければ、 `Downlods/`以下に `google-cloud-sdk-<バージョン>-<OS>-<CPUアーキテクチャ>.tar.gz` のようなファイルが作成されます。)

```shell

# 現在の場所を確認
>> pwd
/home/<ユーザー名>

# (Downloads/以下にgoogle-cloud-sdk~ が保存されていた場合、間違えて消さないようにホームディレクトリに移動する)
>> mv ./Downloads/google-cloud-sdk-

# インストールスクリプトを実行して gcloudコマンドを使えるようにする
# (色々と質問してくるが、基本的にYesとパスワード入力していれば良い)
>> ./google-cloud-sdk/install.sh


```

#### 1-2. Google Cloud SDKを解凍

```shell

# (Downloads/以下にgoogle-cloud-sdk~ が保存されていた場合、間違えて消さないようにホームディレクトリに移動する)
>> mv ./Downloads/google-cloud-sdk~
/home/<ユーザー名>

# インストールスクリプトを実行して gcloudコマンドを使えるようにする
# (色々と質問してくるが、基本的にYesとパスワード入力していれば良い)
>> ./google-cloud-sdk/install.sh


```

#### 1-3. Google Cloud SDK install.shを実行



#### 1-4. Google Cloud SDK を初期化

### 2.
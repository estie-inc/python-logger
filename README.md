python-repository-template
===

Python の repository を作る時に毎回するセットアップをまとめておく。

## 使用方法
基本的にはこの repository の中身をコピーすればOK。必要なのは以下のファイル・フォルダ。

```shell
.
├── .github
├── .gitignore
├── Pipfile
├── Pipfile.lock
├── README.md
├── main.py
├── rename_me
├── setup.py
├── Dockerfile
├── docker-compose.yml
├── Makefile
└── tests
```

### 各 repository ごとに修正するところ
* [README.md](./README.md): それぞれの repository にあった説明に変える。
* [rename_me](./rename_me): source ファイルを入れるフォルダ。 repository に応じて名前を変える。
* [setup.py](./setup.py): `name`, `description`, `url` を上記の source フォルダ名などに応じて変える。
* [docker-compose.yml](./docker-compose.yml): servicesの`python-template`およびコンテナ名の`python_template`を変更する。volumesの`./reaname_me:/var/app/rename_me`内の`rename_me`を上の rename_me フォルダと同じ名前に変える。
* [Makefile](./Makefile): `python-template`となっているところを docker-compose.yml での変更に応じて変更する。

```shell
git grep rename
git grep template
```

などで調べるとよい。

NOTE: このリポジトリ自体は release の概念はないので、 `release` のみを用意している。

以下はそのまま流用可能。

===

# 開発
## 準備
依存関係の解決なども pipenv によって行っているのでインストールする。
また、必要なバージョンをインストールできるように pyenv もインストールしておく。

## Dockerを使わない場合の環境構築
以下のコマンドで依存関係を解消する。

```shell
pipenv install --dev
```

## Docker
### 前提となる環境
- Dockerクライアントがホストマシンにインストールされていること

### macOS での Docker セットアップ
以下のコマンドを実行後、 Docker.app を起動し、`docker ps` 等にてインストールの確認。

```bash
# docker-compose も導入されるはず
brew cask install docker
```
### コンテナの立ち上げ
以下のコマンドで Docker コンテナが立ち上がる。

```shell
make run
```
成功すれば、 `docker ps` でコンテナが起動していることが確認できるはず。


## 実行方法
以下のコマンドで [main.py](./main.py) を実行する。

```shell
make start

# or ローカルで pipenv install --dev すればコンテナを起動せずともこちらでいける(以下同様)

pipenv run start
```


## テスト
```shell
make test

# or

pipenv run test
```

## Linter
```shell
make lint

# or

pipenv run lint
```

自動で修正する場合は以下のコマンドを実行する。

```shell
make format

# or

pipenv run format
```

## Debug
以下のコマンドが利用可能。詳細は[Makefile](./Makefile)を参照のこと。

```
make enter      # コンテナに入る
make log        # ログを見始める
```

# CI
GitHub Actions の config を [`.github/workflows`](./.github/workflows) に記述している。現在は以下の設定になっている。

* すべての commit に対して test が走る。
* release への commit に対して、 `release/{date}_{number}` タグが切られる。

このため、基本的には `dev` ブランチを切って、それを default ブランチに設定し、`release` への commit は `dev` ブランチのマージによって行うと良い。

# pylogger

Python logger for every project using Python.

## 開発

### 準備

依存関係の解決なども poetry によって行っているのでインストールする。
また、必要なバージョンをインストールできるように pyenv もインストールしておく。

#### Dockerを使わない場合の環境構築

以下のコマンドで依存関係を解消する。

```shell
poetry install
```

#### Docker

##### 前提となる環境

- Dockerクライアントがホストマシンにインストールされていること

##### macOS での Docker セットアップ

以下のコマンドを実行後、 Docker.app を起動し、`docker ps` 等にてインストールの確認。

```bash
# docker-compose も導入されるはず
brew cask install docker
```

##### コンテナの立ち上げ

以下のコマンドで Docker コンテナが立ち上がる。

```shell
make run
```

成功すれば、 `docker ps` でコンテナが起動していることが確認できるはず。

***

#### Test

```shell
make test

# or

poetry run test
```

***

#### Linter

```shell
make lint

# or

poetry run lint
```

自動で修正する場合は以下のコマンドを実行する。

```shell
make format

# or

poetry run format
```

***

#### Debug

以下のコマンドが利用可能。詳細は[Makefile](./Makefile)を参照のこと。

```shell
make enter      # コンテナに入る
make log        # ログを見始める
```

***

#### CI

GitHub Actions の config を [`.github/workflows`](./.github/workflows) に記述している。現在は以下の設定になっている。

- すべての commit に対して test が走る。
- release への commit に対して、 `release/{date}_{number}` タグが切られる。

このため、基本的には `dev` ブランチを切って、それを default ブランチに設定し、`release` への commit は `dev` ブランチのマージによって行うと良い。

***

## ディレクトリ構成

```shell
.
├── Dockerfile
├── LICENSE
├── Makefile
├── Pipfile
├── Pipfile.lock
├── README.md
├── docker-compose.yml
├── main.py
├── pylogger
├── pyproject.toml
├── setup.cfg
├── setup.py
└── tests
```

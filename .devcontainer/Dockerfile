FROM mcr.microsoft.com/devcontainers/python:3.11

# 必要なパッケージのインストール
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
  && apt-get -y install --no-install-recommends \
  git \
  curl \
  && apt-get clean -y \
  && rm -rf /var/lib/apt/lists/*

# Pythonの開発ツールのインストール
RUN pip install --upgrade pip \
  && pip install \
  black \
  pylint \
  pytest

# 作業ディレクトリの設定
WORKDIR /workspace

# ユーザー設定
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
  && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
  && apt-get update \
  && apt-get install -y sudo \
  && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
  && chmod 0440 /etc/sudoers.d/$USERNAME 
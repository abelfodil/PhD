FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu-20.04

RUN apt-get update && apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && apt-get update && \
    apt-get install -y build-essential apt-transport-https python3.7 python3.7-venv python3-pip git wget unzip

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1

USER vscode

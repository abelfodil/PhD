FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu-20.04

RUN apt-get update && apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && apt update && \
    apt install -y build-essential apt-transport-https wget unzip python3.7 python3.7-venv python3-pip

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y x11-apps libgtk2.0-dev libgtk-3-dev libsdl2-mixer-2.0-0 libsdl2-image-2.0-0 libsdl2-2.0-0 \ 
    libjpeg-turbo8-dev libtiff5-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libnotify-dev freeglut3-dev && \
    pip install -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-18.04 wxpython fsleyes

ENV FSLDIR /usr/local/lib/python3.7/dist-packages/fsl

USER vscode

RUN cd /tmp && \
    wget https://github.com/spinalcordtoolbox/spinalcordtoolbox/archive/refs/tags/5.4.zip -O sct.zip && \
    unzip sct.zip && \
    cd spinalcordtoolbox-5.4 && \
    ./install_sct -y

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

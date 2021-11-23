from ubuntu:latest

RUN apt update && apt upgrade -y
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt install python3.10 -y
RUN apt install python3-pip -y
RUN apt install nano -y

WORKDIR /wordcount-client
COPY . /wordcount-client

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 4000
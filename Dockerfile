From amd64/ubuntu:18.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip vim

COPY src/ src/

RUN pip3 install -r src/requirements.txt
COPY entrypoint.sh /

EXPOSE 14550
EXPOSE 14551

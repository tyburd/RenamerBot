FROM python:3.9.1-buster
WORKDIR /usr/src/app
ENV DEBIAN_FRONTEND=noninteractive
RUN apt -qq update && apt -qq install -y git python3 python3-pip ffmpeg
COPY . .
RUN pip install -U -r requirements.txt
CMD [ "bash", "start" ]

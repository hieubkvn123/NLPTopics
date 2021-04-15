FROM ubuntu:20.04

RUN apt-get update -y && \
	apt-get install -y python3-pip python3-dev

RUN pip3 install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt
RUN pip3 install h5py==2.10.0
RUN python3 -m nltk.downloader stopwords

COPY . /app

CMD ["python3", "server.py", "--debug", "0", "--port", "8080"]

FROM ubuntu:18.04
RUN apt-get update && apt-get install wget -y && apt install default-jre -y && apt-get install -y openbabel && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-setuptools \
    python3-wheel \
    python3-cffi \
    git \
    && rm -rf /var/lib/apt/lists/* 
COPY . /app
WORKDIR /app
RUN chmod +x /app/mold2/Mold2
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:8080", "server:app" ]
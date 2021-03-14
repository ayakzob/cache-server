FROM python:3.8

WORKDIR /src

COPY requirements.txt /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt

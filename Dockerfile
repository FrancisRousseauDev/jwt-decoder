FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip
COPY requirements.txt /app/
RUN pip3 install --requirement /app/requirements.txt
COPY . /app/
ENTRYPOINT ["python3","/app/main.py"]
CMD ["python3", "/app/main.py"]
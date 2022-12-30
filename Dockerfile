FROM python:3.9-alpine

RUN mkdir -p /home/app

COPY requirements.txt /home/app

RUN pip install -r /home/app/requirements.txt

COPY . /home/app

WORKDIR /home/app

CMD ["python", "main.py"]


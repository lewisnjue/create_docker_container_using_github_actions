FROM python:3.9.21-slim-bookworm

COPY . /app
WORKDIR /app 

RUN pip install -r requirements.txt 

CMD [ "uvicorn", "main:app" ]

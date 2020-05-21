from python:3.6

USER root
WORKDIR /app

COPY requirements.txt .

RUN apt-get -y update

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn" , "--bind" , "0.0.0.0:5000" , "--timeout" , "360" ,"wsgi:app"]
EXPOSE 5000

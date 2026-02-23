FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

RUN apt-get update && apt-get install -y netcat-openbsd
COPY wait-for-db.sh /wait-for-db.sh
RUN chmod +x /wait-for-db.sh

CMD ["/wait-for-db.sh"]
FROM python:3.10

WORKDIR /app

RUN apt update && \
    apt install -y gcc libkrb5-dev && \
    apt clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV DJANGO_SETTINGS_MODULE=enterprise_kpi_tracker.settings
ENV PYTHONUNBUFFERED 1
EXPOSE 3000
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
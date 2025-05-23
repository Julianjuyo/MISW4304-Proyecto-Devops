FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000"]

# New Relic
RUN pip install newrelic
ENV NEW_RELIC_APP_NAME="app_entrega4"
ENV NEW_RELIC_LOG=stdout
ENV NEW_RELIC_DISTRIBUTED_TRACING_ENABLED=true
ENV NEW_RELIC_LOG_LEVEL=info
ENTRYPOINT [ "newrelic-admin", "run-program" ]


# docker build -t entrega4 .
# database
# docker run -d --name postgres_db --network mynet -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgrespwd -e POSTGRES_DB=postgres -p 5432:5432 postgres
# app
# docker run --network mynet -p 5001:5000 -e DB_USER=postgres -e DB_PASSWORD=postgrespwd -e DB_HOST_DOCKER=postgres_db -e DB_PORT=5432 -e DB_NAME=postgres -e NEW_RELIC_LICENSE_KEY=key entrega4

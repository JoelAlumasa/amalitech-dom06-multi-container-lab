# DOM06 - Multi-Container App (Docker Compose)

Services:
- web: Flask app (port 5000)
- db: MySQL 8 (initialized with db/init.sql)

Run:
docker compose up -d --build

Test:
curl -i http://localhost:5000/

Cleanup:
docker compose down --volumes

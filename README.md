# DOM06 - Multi-Container App (Docker Compose)

## Overview
This lab runs a simple multi-container application using Docker Compose:
- **web**: Flask app exposed on port **5000**
- **db**: MySQL 8 initialized with `db/init.sql`

## Local Run (WSL / laptop)
```bash
docker compose up -d --build
docker compose ps
curl -i http://localhost:5000/

Cleanup:
docker compose down --volumes
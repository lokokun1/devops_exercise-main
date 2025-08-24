# DevOps Exercise — Prometheus HTTP Service Discovery

## Whats here
- `inventory_server/` — Flask service exposing `GET /inventory` → `["sensor_0", ...]`
- `adapter/` — Tiny Flask adapter exposing `GET /sd` in Prometheus HTTP-SD format
- `prometheus/` — Prometheus config using `http_sd_configs` → `sd-adapter:8001/sd`
- `docker-compose.yml` — Brings up the whole stack

## Run
```bash
docker compose up --build -d

# curl http://localhost:8001/sd

# http://localhost:1337/inventory

# then go via browser http://localhost:9090/targets and see all the sensors
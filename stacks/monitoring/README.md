# monitoring — Grafana + Prometheus + exporters

Observabilidad del server: métricas del host y de los contenedores, con dashboards en Grafana.

## Qué corre

| Servicio | Puerto | Para qué |
|----------|--------|----------|
| Prometheus | 9090 | Recolecta y almacena métricas |
| node-exporter | (interno) | Métricas del host: CPU, RAM, disco, temperatura |
| cAdvisor | (interno) | Métricas por contenedor |
| Grafana | 3000 | Dashboards |

## Levantar

```bash
cd /opt/stacks/monitoring
docker compose up -d
```

## Setup inicial (una sola vez, se hace en la UI de Grafana)

Grafana guarda su config en un volumen Docker, así que estos pasos se hacen a mano
la primera vez (o si se recrea el volumen). No están versionados todavía —
ver "Pendiente" abajo.

1. Entrar a `http://<host>:3000` — login inicial `admin` / `admin` (obliga a cambiar).
2. **Connections → Data sources → Add → Prometheus.**
   - URL: `http://prometheus:9090` (por nombre de servicio, no IP).
   - **Save & test** → debe salir verde.
3. **Dashboards → New → Import.**
   - ID de grafana.com: `1860` (Node Exporter Full).
   - Data source: Prometheus.
   - **Import.**

El panel de temperatura está en la sección **Hardware Misc → Hardware Temperature Monitor**.
Los sensores aparecen como `coretemp temp*` (núcleos CPU) y `dell_smm temp*` (placa).

## Pendiente / mejora futura

- **Provisioning automático:** el data source y el dashboard se configuran a mano en la UI.
  Se pueden dejar declarados en archivos (provisioning de Grafana) para que al recrear el
  stack todo aparezca solo. Refinamiento, no urgente.
- **Loki (logs):** cuando haya apps generando logs que valga la pena centralizar, se suma
  Loki al stack y se integra con Grafana. Todavía no hace falta.

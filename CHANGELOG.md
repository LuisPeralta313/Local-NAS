# Changelog — Estigia

Formato basado en versionado semántico (SemVer).

## [v1.1.0] — 2026-08-13

### Añadido
- Stack `monitoring/`: Grafana + Prometheus + node-exporter + cAdvisor.
- Dashboard "Node Exporter Full" (grafana.com ID 1860) para CPU, RAM, disco, red y temperatura.
- Verificación térmica del host: núcleos ~50-65°C bajo carga ligera con tapa cerrada (sano).

### Notas
- La configuración de Grafana (data source + dashboard) se hace a mano en la UI por ahora;
  vive en el volumen Docker, no versionada. Provisioning automático queda como mejora futura.

## [v1.0.0] — 2026-08-06

### Añadido
- Fundación del homelab sobre Dell Inspiron 5577 con Ubuntu Server 26.04 LTS (headless).
- Acceso remoto por Tailscale (IP estable, independiente del DHCP local).
- Docker + Docker Compose como runtime de todos los servicios.
- Stacks: `peredent` (placeholder), `data-projects` (Jupyter + Postgres), `jellyfin`,
  `caddy` (reverse proxy), `minecraft`.
- Panel de gestión Dockge.
- Disco LVM expandido a ~914 GB usables; WiFi por dongle TP-Link (driver RTL8188EUS via DKMS);
  arranque con tapa cerrada (`logind.conf`).

### Problemas conocidos
- Caddy → PEREDENT: redirige mal (redes Docker separadas). Pendiente de arreglo.
- PEREDENT es solo placeholder; sin código real todavía.

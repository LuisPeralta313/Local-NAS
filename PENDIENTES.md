# Pendientes y siguientes pasos — Estigia

> Lista viva. Lo tachado con [x] ya está hecho.

---

## Hecho

- [x] **Monitoreo (Grafana + Prometheus + node-exporter + cAdvisor).** v1.1.0.
      Dashboard Node Exporter Full (ID 1860). Temperatura del host verificada.

## Ruta DevOps (hecho en orden, cada pieza cuando el proyecto la pida)

1. [x] **Grafana / monitoreo** — hecho.
2. [ ] **Gitea** — Git self-hosted propio (base para el CI). SIGUE AQUÍ.
3. [ ] **CI (Gitea Actions)** — pruebas automáticas al hacer push.
4. [ ] **CD** — despliegue controlado (para PEREDENT: staging + self-hosted runner
       conectado al GitHub actual, desplegar "cuando yo lo vea bien").
5. [ ] **Capa Sec (DevSecOps)** — Trivy (escaneo de imágenes), Gitleaks (secretos),
       Dependabot (ya en GitHub). SonarQube más adelante.

## Otros pendientes

- [ ] **Arreglar Caddy → PEREDENT** (redes Docker separadas; misma red o host.docker.internal).
- [ ] **Minecraft multi-mundo** — guardar varios mundos y elegir cuál se levanta.
- [ ] **Jellyfin** — investigar descarga/búsqueda de películas y documentarlo.
- [ ] **Config fina** — revisar Tailscale; Dockge ya instalado (v1.0.x).
- [ ] **Provisioning de Grafana** — dejar data source + dashboard como archivos (auto al recrear).
- [ ] **PEREDENT** — meter código real y definir stack (aún NO empezado, proyecto Universidad, ignorar a quien competa) 

## Congelado -- No ahora --

- **Terraform** — solo tiene sentido cuando se toque infraestructura en la nube (VPS/AWS/GCP).
  Con un solo server físico, el IaC real son los docker-compose. Reevaluar al ir a cloud.
- **ZimaOS** — es un SO completo (reemplazaría Ubuntu), no una app. Para otra máquina algún día.
  Para explorar catálogo de servicios: Awesome-Selfhosted / LinuxServer.io, montados como stacks, además de permitir tener un sv redundante o específico para IoT u otra cosa interesante del ZimaOS(pero sí, para otra máquina, no este sv) 


--
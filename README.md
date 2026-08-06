# Estigia — Homelab Self-Hosted

> Servidor casero sobre una laptop Dell reutilizada (i5-7300HQ, 16 GB RAM, 1 TB HDD, GTX 1050).
> Corre Ubuntu Server 26.04 LTS headless, con acceso remoto por Tailscale y servicios en Docker. ( Considero las posibles vulnerabilidades de la versión y las manejo de la mejor forma al no exponerme ) 
> Todo es IaC: cada servicio vive en su propia carpeta con su `compose.yaml`, se levanta y se baja
> de forma independiente, y vuelve solo tras un reinicio.

---

## Cómo interactúa todo (vista de pájaro)

```
                       INTERNET
                          │
                    (WiFi TP-Link)
                          │
            ┌─────────────▼─────────────┐
            │      ESTIGIA (host)        │
            │   Ubuntu Server 26.04      │
            │                            │
            │   Tailscale ── acceso remoto seguro (SSH desde
            │      │        cualquier lugar, sin abrir puertos)
            │      │                     │
            │   Docker ── runtime de todos los servicios
            │      │                     │
            │      ├── peredent/     (web app + PostgreSQL)
            │      ├── data-projects/(Jupyter + PostgreSQL)
            │      ├── jellyfin/     (media server)
            │      ├── caddy/        (reverse proxy → expone la web)
            │      └── minecraft/    (game server)
            └────────────────────────────┘
```

**La idea central:** el host se mantiene limpio y aburrido. Todo lo interesante vive dentro de
contenedores, aislado, reproducible y desechable. Si un servicio explota, no toca a los demás.

---

## Por qué está diseñado así

- **Un stack = una carpeta = un `compose.yaml`.** Cada servicio es independiente. Lo levantas con
  `docker compose up -d` dentro de su carpeta, y lo bajas con `docker compose down`. Nada se mezcla.
- **`restart: unless-stopped` en todo.** Si se va la luz o se reinicia el host, Docker vuelve a
  levantar lo que estaba corriendo. Ese es el "self-healing" — no hay que tocar nada a mano.
- **Tailscale en vez de abrir puertos.** El router de esta red no es administrable (solo se tiene la
  contraseña del WiFi). Tailscale crea una red malla cifrada entre dispositivos y atraviesa el NAT
  sin configurar nada en el router. El acceso remoto deja de depender de la red local.
- **Caddy como única puerta pública.** Cuando un servicio necesita ser visto desde internet
  (ej. un cliente revisando la web app), Caddy lo expone; el resto queda solo en la red privada.
- **LVM sin cifrado.** El disco usa LVM (flexible para redimensionar) pero sin LUKS: un servidor
  always-on headless no puede pedir contraseña de descifrado en cada arranque.

---

## Tecnologías usadas

| Capa | Herramienta | Para qué |
|------|-------------|----------|
| SO host | Ubuntu Server 26.04 LTS | Base headless, soporte hasta 2031 |
| Acceso remoto | Tailscale (WireGuard) | SSH desde cualquier lugar, sin abrir puertos |
| Runtime | Docker + Docker Compose | Aislar y orquestar servicios |
| Web app | FastAPI + PostgreSQL | Backend + base de datos del proyecto |
| Data/ML | Jupyter Lab + PostgreSQL | Workspace de análisis y modelos |
| Media | Jellyfin | Servir video/archivos multimedia |
| Reverse proxy | Caddy | Exponer la web app públicamente |
| Game server | itzg/minecraft-server | Servidor de Minecraft Java |

---

## Estructura del repositorio

```
/opt/stacks/
├── peredent/            # Web app con base de datos (plantilla, mete tu código en src/)
│   ├── compose.yaml
│   ├── .env.example     # Copiar a .env y rellenar
│   └── src/
│       ├── Dockerfile
│       ├── requirements.txt
│       └── main.py
│
├── data-projects/       # Jupyter + PostgreSQL para análisis/ML
│   ├── compose.yaml
│   └── .gitignore       # Ignora datasets/ y datos pesados
│
├── jellyfin/            # Media server
│   └── compose.yaml
│
├── caddy/               # Reverse proxy
│   ├── compose.yaml
│   └── Caddyfile
│
└── minecraft/           # Game server
    └── compose.yaml
```

---

## Cómo levantar cada servicio

```bash
# Levantar uno
cd /opt/stacks/<servicio>
docker compose up -d

# Ver qué corre
docker ps

# Ver logs de uno
docker compose logs -f

# Bajar uno
docker compose down
```

Cada carpeta tiene su propio ciclo de vida. No hace falta levantar todo a la vez.

---

## Notas de reproducción

- `version:` en los `compose.yaml` es obsoleto en Docker Compose moderno; se puede omitir.
- Los valores de contraseñas están como *placeholders*. Copia cada `.env.example` a `.env`
  y pon valores reales (el `.env` nunca se sube a Git).
- El firmware/host es específico: kernel reciente para soportar el WiFi integrado y el dongle USB.
- Este repo documenta *estructura y decisiones*, no incluye datos ni secretos.

---

## Ideas y posibles expansiones futuras

Ver [`IDEAS.md`](./IDEAS.md).

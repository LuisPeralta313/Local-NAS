# Ideas y posibles expansiones futuras

Ideas que surgieron durante el armado del homelab y que quedan como terreno para explorar.
No son compromisos, son direcciones.

---

## Infraestructura / plataforma

- **Obsidian con Git selectivo.** Versionar solo una subcarpeta del vault (ej. `07-universidad/`)
  contra un repo en el servidor, usando `git subtree` o un submódulo, para subir/bajar cambios de
  esa área sin exponer el resto del vault. Pendiente validar el flujo exacto.
- **Reverse proxy con HTTPS automático.** Caddy puede emitir certificados Let's Encrypt solo si hay
  un dominio apuntando al servidor. Registrar un dominio barato y darle URLs limpias a los servicios
  en vez de IP:puerto.
- **Backups automáticos.** Un contenedor tipo `restic`/`borg` que respalde los volúmenes de datos
  (bases de datos, configs) a almacenamiento externo o a otra máquina, de forma programada.
- **IP fija o reserva DHCP.** La IP local cambia entre reinicios; Tailscale ya da un nombre estable,
  pero reservar la IP en el router (si algún día hay acceso) simplificaría el acceso en LAN.
- **Segunda NIC / mejor antena.** El WiFi es el cuello de botella. Un adaptador USB-Gigabit + cable,
  o una antena externa, subirían mucho la estabilidad y el throughput.
- **Monitoreo.** Un stack de observabilidad (Prometheus + Grafana, o algo ligero como Beszel) para
  ver CPU, RAM, disco, temperatura y estado de contenedores desde un dashboard. Importante. 
- **tmux por defecto.** Envolver procesos largos en `tmux` de forma sistemática para que sobrevivan
  a cortes de SSH (lección aprendida a las malas).

---

## Servicios nuevos

- **Nextcloud.** Para archivos personales estilo Dropbox (subir desde laptop/teléfono al servidor).
  Distinto de Jellyfin, que es solo para media.
- **Gitea.** Servidor Git propio para hospedar repos privados y dar acceso limitado a colaboradores
  con permisos por repositorio.
- **Panel visual (Dockge / Portainer / CasaOS).** Gestionar contenedores desde una UI web. Útil para
  no depender siempre de la terminal; CasaOS además trae un "app store" para instalar servicios
  (incluido Minecraft) con un clic.
- **Ollama + modelo pequeño.** Correr un LLM local ligero para experimentos de IA/agentes, aprovechando
  la GPU para inferencia modesta.

---

## Multi-tenant / colaboración

- **Entornos aislados por persona.** Una instancia de la web app + su base de datos por cada
  colaborador, cada una en su carpeta y sus puertos, sin verse entre sí. Es el patrón real de
  *multi-tenancy* llevado a escala casera; buen ejercicio de arquitectura.
- **Ambientes dev / staging / prod.** El mismo proyecto en tres versiones: una para romper, una para
  probar, una "de verdad". Practicar el flujo de promoción entre ambientes.

---

## Flujos de datos (perfil Data / BI / ML)

- **Pipeline real de datos.** Captura (ingesta) → limpieza → análisis → visualización, cada etapa
  como un paso reproducible que se levanta y se baja bajo demanda.
- **Orquestación.** Agregar un orquestador (Airflow o similar) para correr pipelines programados,
  y así poder hablar de orquestación en una entrevista con algo real detrás.
- **Almacenamiento de proyectos terminados.** Convención para archivar un proyecto (código +
  notebook + esquema de datos) de forma que se pueda volver a levantar y re-descargar el dataset
  cuando se necesite, sin guardar datasets pesados en Git.

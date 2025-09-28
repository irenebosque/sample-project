
## Estructura del Proyecto

```
exampleProject/
├── .env                           # Variables de entorno
├── .env.example                   # Ejemplo de variables de entorno
├── .gitignore                     # Archivos ignorados por Git
├── README.md                      # Documentación del proyecto
├── docker-compose.yml             # Configuración de Docker Compose
└── src/
    └── main/
        ├── docker/
        │   ├── backend/
        │   │   └── Dockerfile     # Dockerfile para el backend Python
        │   ├── nginx/
        │   │   ├── Dockerfile     # Dockerfile para nginx
        │   │   └── nginx.conf     # Configuración de nginx (reverse proxy)
        │   └── nuxt/
        │       └── Dockerfile     # Dockerfile para el frontend Nuxt
        ├── nuxt/                  # Frontend Nuxt.js
        │   ├── .nuxt/             # Archivos generados por Nuxt (build)
        │   ├── node_modules/      # Dependencias de Node.js
        │   ├── server/
        │   │   └── api/
        │   │       └── random-word.get.ts  # API endpoint para palabras aleatorias
        │   ├── app.vue            # Componente principal de Vue
        │   ├── nuxt.config.ts     # Configuración de Nuxt
        │   ├── package.json       # Dependencias del frontend
        │   └── package-lock.json  # Lockfile de dependencias
        └── python/                # Backend Python
            ├── api/
            │   ├── __init__.py
            │   └── random_word_api.py  # API para palabras aleatorias
            ├── main.py            # Punto de entrada de FastAPI
            └── requirements.txt   # Dependencias de Python
```


## Para lanzarlo en local

### Opción 1: Con Docker (Recomendado)

**Desarrollo (por defecto):**
```bash
# Construir y levantar
docker compose up --build

# Solo levantar
docker compose up

# En segundo plano
docker compose up -d
```

**Producción:**
```bash
# Cambiar a target production y construir
docker compose build --build-arg TARGET=production frontend

# O modificar temporalmente el docker-compose.yml cambiando 'target: development' por 'target: production'
```

**Comandos generales:**
```bash
# Parar los servicios
docker compose down

# Parar y eliminar volúmenes
docker compose down -v

# Reconstruir todo desde cero
docker compose build --no-cache
```

Esto levantará todos los servicios:
- **nginx**: Puerto 80 (reverse proxy)
- **backend**: Puerto 8000 (FastAPI)
- **frontend**: Puerto 3000 (Nuxt.js)

Accede a la aplicación en: http://localhost

### Opción 2: Manual

**Backend:**
```bash
uvicorn src.main.python.main:app --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
cd src/main/nuxt
npm install  # solo la primera vez
npm run dev
```



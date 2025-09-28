# Build Stage 1
FROM node:22-alpine AS build
WORKDIR /app

RUN corepack enable

# Copiar package.json y package-lock.json
COPY package*.json ./

# Instalar dependencias
RUN npm install

# Copiar el resto del código
COPY . ./

# Build el proyecto
RUN npm run build

# Build Stage 2
FROM node:22-alpine
WORKDIR /app

# Solo la carpeta .output es necesaria del build stage
COPY --from=build /app/.output/ ./

# Cambiar puerto y host
ENV PORT=3000
ENV HOST=0.0.0.0

EXPOSE 3000

CMD ["node", "/app/server/index.mjs"]
#!/bin/bash

# 1. Crear el Dockerfile dinámicamente
echo "Cretating Dockerfile..."
cat << END > Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
END

# 2. Construir la imagen
echo "Building Docker image..."
docker build -t shodan-app .

# 3. Ejecutar el contenedor
# Pasamos las variables de entorno necesarias. 
# Nota: En Jenkins, estas variables se configuran en el Job.
echo "Running container..."
docker run --name samplerunning \
  -e SHODAN_API_KEY=\$SHODAN_API_KEY \
  -e TARGET_IP=\$TARGET_IP \
  shodan-app

# 4. Generar evidencias para el archivo output.txt (Requisito de la rúbrica)
echo "Generating output.txt..."
echo "--- ESTADO DEL CONTENEDOR (docker ps -a) ---" > output.txt
docker ps -a --filter "name=samplerunning" >> output.txt
echo -e "\n--- LOGS DE LA APLICACIÓN (Datos de API) ---" >> output.txt
docker logs samplerunning >> output.txt

echo "Proceso finalizado con éxito."

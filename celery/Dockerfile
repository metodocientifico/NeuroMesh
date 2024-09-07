FROM python:3.9

# Establecer directorio de trabajo
WORKDIR /usr/src/app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . .

# Exponer el puerto
EXPOSE 8000

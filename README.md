
# NeuroMesh

**NeuroMesh** es un stack de desarrollo que unifica inteligencia artificial, desarrollo web en Django, procesamiento de tareas asíncronas con Celery y RabbitMQ, y almacenamiento de datos no relacional con MongoDB. Este stack está optimizado para la experimentación con modelos de IA y la ejecución de aplicaciones web escalables, con tareas automáticas y preconfiguraciones listas para comenzar rápidamente.

## Servicios incluidos

- **Django**: Framework web en Python.
- **Celery**: Manejo de tareas asíncronas, ideal para procesamiento en segundo plano.
- **Redis**: Almacenamiento en caché y backend para Celery.
- **RabbitMQ**: Broker de mensajes para Celery, utilizado para gestionar las colas de tareas.
- **MongoDB**: Base de datos no relacional para almacenamiento de datos estructurados o no estructurados.
- **Jupyter Notebooks**: Entorno interactivo para experimentación con modelos de inteligencia artificial y visualización de datos.

## Pre-requisitos

Antes de iniciar, asegúrate de tener instalados los siguientes programas en tu máquina:

- [Docker](https://www.docker.com/get-started) - Requerido para construir y ejecutar los contenedores.
- [Docker Compose](https://docs.docker.com/compose/install/) - Para orquestar los contenedores.

## Estructura del Proyecto

```
NeuroMesh/
├── app/
│   ├── Dockerfile               # Dockerfile para Django
│   ├── manage.py                # Script de administración de Django
│   ├── myapp/                   # Directorio principal de la app Django
│       ├── __init__.py
│       ├── settings.py          # Configuración de Django
│       ├── tasks.py             # Tareas preconfiguradas para Celery
│       ├── urls.py              # Rutas de Django
│       └── wsgi.py              # Configuración WSGI
├── celery/
│   ├── Dockerfile               # Dockerfile para Celery
├── notebooks/
│   └── example.ipynb            # Jupyter Notebook para desarrollo de IA
├── rabbitmq/
├── mongodb/
├── docker-compose.yml           # Configuración Docker Compose para todos los servicios
├── requirements.txt             # Dependencias del proyecto
├── .env                         # Variables de entorno
└── README.md                    # Documentación del proyecto
```

## Instalación

1. **Clonar el repositorio:**

```bash
git clone https://github.com/tu-usuario/NeuroMesh.git
cd NeuroMesh
```

2. **Configuración de Variables de Entorno:**

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```bash
POSTGRES_DB=django_db
POSTGRES_USER=django_user
POSTGRES_PASSWORD=django_password
```

Asegúrate de ajustar las variables si es necesario.

3. **Construir y levantar los servicios:**

```bash
docker-compose up --build
```

Este comando descargará las imágenes de Docker necesarias, construirá los contenedores y levantará el stack. Además, Django ejecutará automáticamente las migraciones de la base de datos, y **Celery** tendrá una tarea preconfigurada lista para usarse.

4. **Acceder a los servicios:**

- **Django**: Navega a `http://localhost:8000` para ver la aplicación web.
- **Jupyter Notebooks**: Accede a `http://localhost:8888` para comenzar a trabajar con tus notebooks de IA.
- **RabbitMQ**: Administra RabbitMQ en `http://localhost:15672` (usuario: `guest`, contraseña: `guest`).

## Primeros pasos con Django

1. **Crear superusuario:**

```bash
docker-compose exec django python manage.py createsuperuser
```

Sigue las instrucciones para crear un superusuario con el que puedas acceder al **admin panel** de Django en `http://localhost:8000/admin/`.

2. **Agregar una tarea con Celery**:

Celery viene preconfigurado con una tarea de ejemplo que puedes ejecutar fácilmente. Esta tarea se encuentra en `app/myapp/tasks.py`.

**Ejemplo de ejecución de una tarea:**

Abre una consola dentro del contenedor Django:

```bash
docker-compose exec django python manage.py shell
```

Luego, ejecuta la tarea:

```python
from myapp.tasks import example_task
example_task.delay()
```

Esto añadirá una tarea a la cola de RabbitMQ y será procesada por el worker de Celery.

## Contribución

Este stack es escalable y extensible. Si deseas agregar más servicios o mejorar la infraestructura, siéntete libre de hacer un fork y enviar PRs o sugerencias.


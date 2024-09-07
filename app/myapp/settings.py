# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_db',
        'USER': 'django_user',
        'PASSWORD': 'django_password',
        'HOST': 'db',
        'PORT': '5432',
    }
}

# Configuración de Celery para Redis y RabbitMQ
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_BROKER_ALTERNATE_URLS = ['amqp://rabbitmq:5672']

# MongoDB para IA
MONGO_DB_NAME = 'ai_db'
MONGO_URI = 'mongodb://mongodb:27017/'

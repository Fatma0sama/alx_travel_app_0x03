# Celery settings
CELERY_BROKER_URL = 'amqp://localhost'  # assuming RabbitMQ is running locally
CELERY_RESULT_BACKEND = 'rpc://'  # or you can use 'django-db' if django-celery-results installed

# Email settings (example using console backend for testing)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@alxtravel.com'

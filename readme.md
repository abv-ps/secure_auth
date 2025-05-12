## Initial project setup

1. **Create a `.env` file** in the root directory with the following keys:
    DJANGO_SECRET_KEY=your_key
    DJANGO_DEBUG=True (for local development)
2. **Install requirements**:
    pip install -r requirements.txt
3. **Create superuser**:
    python manage.py createsuperuser
4. By default, it is configured to run with self-signed certificates via runserver_plus:

run:
python manage.py runserver_plus --cert-file cert.crt

To set them up

sudo apt-get install openssl

openssl genpkey -algorithm RSA -out cert.key -aes256

openssl req -new -x509 -key cert.key -out cert.crt -days 365

The application will be available at: https://localhost:8000

5. If you want to launch without https:

settings.py

if DEBUG:
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False

run:
python manage.py runserver_plus

The application will be available at: http://localhost:8000

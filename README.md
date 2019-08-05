DJANGO LOGIN APP
---------------------------------------------------------------------------------------------------------------------

Aplicación desarrollada con Django 2.2 en que se muestra un ejemplo de "login" y "log out".

La aplicación se conecta a una base de datos PostgreSQL utilizando las librerias psycopg2 y dj_database_url.

---------------------------------------------------------------------------------------------------------------------

**Se configura un custom user model:**

```

from django.contrib.auth.models import AbstractUser
from django.db import models


class AppUser(AbstractUser):
    full_name = models.CharField(max_length=180)

    class Meta:
        ordering = ["full_name"]
    
    def __str__(self):
        return "[User: " + self.username + " - Email: " + self.email + "]"


```

**Configuración en archivo settings:**

```

AUTH_USER_MODEL = 'main.AppUser'

```

---------------------------------------------------------------------------------------------------------------------

**Se define la variable de ambiente "DATABASE_URL" utilizada por la librería dj-database-url**
**para acceder a la base de datos:**

```

DATABASE_URL="postgres://user:password@server:port/name-db"

```

**Configuración de base de datos PostgreSQL en archivo setting.py:**

```

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
    }
}

DATABASES['default'] = dj_database_url.config(conn_max_age=600)

```

---------------------------------------------------------------------------------------------------------------------

**Pantalla de login:**

![Screenshot Login](screenshots/django-login-page.png)


**Pantalla principal a la que se accede cuando se inicia sesión correctamente:**

![Screenshot LoginOK](screenshots/django-successfull-login.png)


**Acceso a opción de log out:**

![Screenshot Logout](screenshots/django-logout-option.png)

---------------------------------------------------------------------------------------------------------------------
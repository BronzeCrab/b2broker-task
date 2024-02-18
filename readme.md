## what is this:

This is django, djangorestframework related task

## how to run it:

Create venv using whatever method you want, example:
```bash
mkvirtualenv django-task
```

Activate it:
```bash
workon django-task
```

Rename `.env_example` to `.env` and fill it with some values:
```bash
mv ./.env_example ./.env
```

Install some dependecies:
```bash
pip install -r requirements.txt
```

Apply some migrations:
```bash
python manage.py migrate
```

Create some superusers:
```bash
python manage.py createsuperuser
```

Go check some admin of this app (go to `/admin`)

Run the project:
```bash
python manage.py runserver
```

## how to run tests:

```bash
python manage.py test
```

## how to test API manually:

### 1 step - run sever:

```bash
python manage.py runserver
```

then:

### 2 step - make http request to create token, then copy token:
```bash
curl --data "password=user_0&username=user_0" http://localhost:8000/api-token-auth/
```

Copy that obtained token and paste it into `check_api.py` script in the root of the project.

then:

### 3 step - run script for test:

```bash
python check_api.py
```
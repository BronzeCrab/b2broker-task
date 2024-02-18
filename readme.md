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

Run the project:
```bash
python manage.py runserver
```

## how to run tests:

```bash
python manage.py 
```
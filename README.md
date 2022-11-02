# Salt-Login
Django Login/Signup Implementation 

## How to setup locally?

### Using Source Code
- Clone the repository using git clone
```
$ git clone https://github.com/PragatiVerma18/Salt-Login/
$ cd Salt-Login
```

- Create a virtual env and install python dependencies from `requirements.txt`
```
$ python3.7 -m venv .venv 
$ . .venv/bin/activate
$ pip install -r requirements.txt 
```

- Run migrations

```
$ python manage.py migrate
```
- Create a superuser to access the admin panel
```
$ python manage.py createsuperuser
```
- Run the server
```
$ python manage.py runserver
```

- Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the website.

## Hosted Link
Heroku - [https://salt-login.herokuapp.com/](https://salt-login.herokuapp.com/)

---

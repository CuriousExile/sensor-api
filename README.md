# Django PI Temperatur Sensor API

> Features: 

- ✅ `be able to push new temperature data set`
- ✅ `pull specific data range of temperature sets`
- ✅ `force temperature update`

<br />

## Manual Build 

> 👉 Download the code  

```bash
$ git clone git@github.com:CuriousExile/sensor-api.git
$ cd sensor-api
```

<br />

> 👉 Install modules via `VENV`  

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Create the Superuser

```bash
$ python manage.py createsuperuser
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver http://127.0.0.1:8001/
```

At this point, the app runs at `http://127.0.0.1:8001/`. 

<br />

## Codebase structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/                            
   |    |-- settings.py   # Project Configuration  
   |    |-- urls.py       # Project Routing
   |
   |-- home/
   |    |-- views.py      # Temperature API Views 
   |    |-- models.py     # API Temperature Data Set Models 
   |
   |-- requirements.txt   # Project Dependencies
   |-- manage.py          # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />
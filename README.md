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
$ python manage.py runserver '127.0.0.1:8001'
```

At this point, the app runs at `127.0.0.1:8001`. 

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

   ## API Usage

   Take current temperate from Pi, adds it to the table and returns the value.
    ```bash
    HTTP GET /v1/temperature/now
    ```
    <br/>
    Return last entry of the database
    ```bash
    HTTP GET /v1/temperature/latest
    ```
    <br/>
    Returns an QuerySet of all temperatures between given dates
    ```bash
    HTTP GET /v1/temperature/range/?start_date=2023-12-31T00:00:00&end_date=2024-12-31T00:00:00
    ```
   <br/>
    Adds costum temperature value (takes a json with following structure in the request body)
    the default value is current time

    ```bash
    HTTP POST /v1/temperature/create

    {
    "sourcename": "SensorName",
    "temperature": 25.5
    }
    ```


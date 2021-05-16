# To Convert address to latitude and longitude after saving in admin panel through django models

## Steps to install

```python

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver


```


## Add your Google maps geocode API Key in models.py file 

[API Link](https://console.cloud.google.com/apis/library/geocoding-backend.googleapis.com)

## Goto admin panel. Create a new address and save :smiley:
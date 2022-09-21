# Real time crypto currency update

## Using local server

1. Create a virtual environment and install the packages using 'python3 -m pip install -r requirements.txt'
2. Run `python manage.py runserver`
3. Open another terminal to run redis using `redis-server`
4. Open two different terminal to start celery-beat and celery worker using `celery -A crypto_tracking beat -l info` and 
  `celery -A crypto_tracking worker -l info` respectively
5. Open Postman to hit the endpoint `http://127.0.0.1:8000/api/price/btc?date=<dd-mm-YYYY>` to test or you can do it locally


## Using Docker
1. Install Docker 
2. docker-compose up --build 


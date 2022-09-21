import os
import requests 
import logging
from crypto_tracking.celery import app

from .models import Price

logger = logging.getLogger(__name__)

max_price = os.environ.get('MAX_PRICE')
min_price = os.environ.get('MIN_PRICE')

@app.task
def get_crypto_data():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&include_last_updated_at=true"
    data = requests.get(url).json()
    price = data['bitcoin']['usd']
    market_cap = data['bitcoin']['usd_market_cap']

    try:
        relation, _ = Price.objects.get_or_create(price=price, market_cap= market_cap)
        logger.info("Data Caputered Successfully.")
    except Exception:
        logger.error("Unable to store the data")

    if price<min_price or price>max_price:
        pass
    
    







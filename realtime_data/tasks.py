from curses.ascii import EM
import os
from tkinter import E
import requests 
import logging
from django.core.mail import send_mail

from crypto_tracking.celery import app
from crypto_tracking.settings import EMAIL_HOST_USER, MAX_PRICE, MIN_PRICE

from .models import Price

logger = logging.getLogger(__name__)

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

    current_price = float(price)
    if current_price<MIN_PRICE or current_price>MAX_PRICE:
        if current_price<MIN_PRICE:
            alert_message = "below the minimum" 
        else:
            alert_message = "above the maximum"

        send_mail(
            "Price Alert",
            "Current Price is {} price (set-up by you)-{} USD".format(alert_message, current_price),
            EMAIL_HOST_USER,
            ["ranjan.rahul970@gmail.com"],
        )
        logger.info("Successfully email sent")

    
    







from django.shortcuts import render
import requests
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator

# Create your views here.
def get_price_details(request):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&include_last_updated_at=true"
    data = requests.get(url).json()
    price = data['bitcoin']['usd']
    market_cap = data['bitcoin']['usd_market_cap']

    context = {'data': data}
    return JsonResponse(context)


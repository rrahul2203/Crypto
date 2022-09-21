import requests
from collections import OrderedDict
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from datetime import datetime
from .models import Price
from .serializer import PriceSerializers


# Create your views here.
def get_price_details(request):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&include_last_updated_at=true"
    data = requests.get(url).json()
    context = {'data': data}
    return JsonResponse(context)


class QueryDatewise(ListAPIView, LimitOffsetPagination):
    queryset = Price.objects.all()
    serializer_class = PriceSerializers

    default_limit=20
    max_limit = 100
    
    def paginate_queryset(self, queryset, request, view=None):
        self.limit = self.get_limit(request)
        if self.limit is None:
            return None

        self.count = self.get_count(queryset)
        self.offset = self.get_offset(request)
        self.request = request
        if self.count > self.limit and self.template is not None:
            self.display_page_controls = True

        if self.count == 0 or self.offset > self.count:
            return []
        return list(queryset[self.offset:self.offset + self.limit])

    def get_paginated_response(self, data):
        current_url = self.get_html_context()['page_links'][1]
        return Response(OrderedDict([
            ('url', current_url),
            ('next', self.get_next_link()),
            ('count', self.count),
            ('results', data)
        ]))


    def get(self, request):
        datestring= request.GET.get('date')
        date = datetime.strptime(datestring, '%d-%m-%Y')
        filter_query = {"created_on__year":date.year, "created_on__month":date.month, "created_on__day":date.day}
        queryset =  Price.objects.filter(**filter_query).order_by('created_on')
        page = self.paginate_queryset(queryset, request)
        print("request ", request)

        serializer_context = {'request': request}
        serializer = self.serializer_class(
            page, context=serializer_context, many=True
        )
        print("serializer ", serializer, "serializer.data", serializer.data )
        return self.get_paginated_response(serializer.data)
    

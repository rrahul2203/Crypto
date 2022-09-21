from rest_framework import serializers
from .models import Price


class PriceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['id', 'price', 'market_cap', 'created_on']
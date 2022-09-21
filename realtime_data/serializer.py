from rest_framework import serializers
from .models import Price


class PriceSerializers(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(source='created_on')
    price = serializers.DecimalField(max_digits=64, decimal_places=2)
    coin = serializers.SerializerMethodField('get_from_coin')
    class Meta:
        model = Price
        fields = ['timestamp', 'price', 'coin' ]

    def get_from_coin(self, Price):
        return 'btc'
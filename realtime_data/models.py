from django.db import models

# Create your models here.
class Price(models.Model):
    id = models.BigAutoField(primary_key=True)
    #coin = models.CharField(max_length=20, blank=True, null=True)
    price = models.CharField(max_length= 200,blank=True, null=True)
    market_cap = models.CharField(max_length= 200, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

        

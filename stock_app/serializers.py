from dataclasses import field
from rest_framework import serializers

from article_app.models import article_details,article_sale

class DetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = article_details
        fields = ('article_name','article_code','article_size','article_colour')
        
class SalesSerializers(serializers.ModelSerializer):
    class Meta:
        model = article_sale
        fields = ('article_id','selling_date','cost_price','selling_price','customer_name')
        
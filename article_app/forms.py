from dataclasses import field, fields
from django.forms import ModelForm
from .models import article_details,article_sale

class create_product_form(ModelForm):
    class Meta:
        model = article_details
        fields = ['article_name','article_code','article_size','article_colour','article_image']

class add_sales_form(ModelForm):
    class Meta:
        model = article_sale
        fields = ['article_id','selling_date','cost_price','selling_price','customer_name']
        
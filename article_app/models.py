from django.db import models

# Create your models here.

class article_details(models.Model):
    article_name = models.CharField(max_length=200)
    article_code =models.CharField(max_length=200)
    article_size = models.CharField(max_length=50)
    article_colour = models.CharField(max_length=100)
    article_image = models.ImageField(upload_to='products/',default='NA')
    
    def __str__(self):
        return (self.article_name)+'*|*'+(self.article_code)+'*|*'+(self.article_size)+'*|*'+(self.article_colour)
        
    
class article_sale(models.Model):
    article_id = models.ForeignKey(article_details,on_delete=models.CASCADE)
    selling_date = models.DateField()
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10,decimal_places=2)
    customer_name = models.TextField(max_length=100)
    
    def __str__(self):
        return (self.article_id+str(self.selling_date)+self.customer_name)
    
    
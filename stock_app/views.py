from rest_framework import viewsets
from article_app.models import article_details,article_sale
from .serializers import DetailsSerializers,SalesSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

class DetailsViewSet(viewsets.ModelViewSet):
   queryset = article_details.objects.all()
   serializer_class = DetailsSerializers


class SalesViewSet(viewsets.ModelViewSet):
   queryset = article_sale.objects.all()
   serializer_class = SalesSerializers
   
@api_view(["GET"])   
def list_article(request):
    articles = article_details.objects.all()
    serializer = DetailsSerializers(articles,many=True)
    content = {'articles':serializer.data}
    return Response(content)
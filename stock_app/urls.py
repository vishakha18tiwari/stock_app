"""stock_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication_app.views import signup_page, tupphomeshop, login_page, logout_page
from article_app.views import home_page, add_products , view_products, edit_product, delete_product, update_product ,add_product_sales, view_sales, edit_sales, delete_sales
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home_page),
    path('login/',login_page),
    path('logout/',logout_page),
    path('tupphomeshop/',tupphomeshop),
    path('signup/',signup_page),
    path('addproducts/',add_products),
    path('viewproducts/',view_products),
    path('edit_product/<int:i>/',edit_product),
    path('delete_product/<int:i>/',delete_product),
    path('edit_product/update_product/<int:i>/',update_product),
    path('addproductsale/<int:i>/',add_product_sales),
    path('view_sales/',view_sales),
    path('edit_sales/<int:i>/',edit_sales),
    path('delete_sales/<int:i>',delete_sales),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
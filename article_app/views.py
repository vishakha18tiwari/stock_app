from email import message
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from .forms import create_product_form , add_sales_form
from .models import article_details, article_sale
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home_page(request):
    return render(request,'home.html')

@login_required
def add_products(request):
    form = create_product_form()
    message=''
    if request.method == 'POST':
        form = create_product_form(request.POST, request.FILES)
        if form.is_valid():
            obj = article_details()
            obj.article_name = form.cleaned_data['article_name']
            obj.article_code = form.cleaned_data['article_code']
            obj.article_size = form.cleaned_data['article_size']
            obj.article_colour = form.cleaned_data['article_colour']
            obj.article_image = form.cleaned_data['article_image']
            obj.save()
            return redirect('/home/')
        message = "please fill form correctly"
    return render(request,'add_products.html',context={'form':form,'message':message})

def view_products(request):
    articles = article_details.objects.all()
    return render(request,'view_products.html',context={'articles':articles})

@login_required            
def edit_product(request,i):
    product = article_details.objects.get(id=i)
    templates = loader.get_template('update_product.html')
    context= {
        'product':product,
              }
    return HttpResponse(templates.render(context,request))

@login_required
def update_product(request,i):
    p_article_name = request.POST['article_name']
    p_article_code = request.POST['article_code']
    p_article_size = request.POST['article_size']
    p_article_colour = request.POST['article_colour']
    product = article_details.objects.get(id=i)
    product.article_name = p_article_name
    product.article_code = p_article_code
    product.article_size = p_article_size
    product.artilce_colour = p_article_colour
    product.save()
    return redirect('/home/')

@login_required
def delete_product(request,i):
    product = article_details.objects.filter(id=i)
    product.delete()
    return redirect('/viewproducts/')

@login_required
def add_product_sales(request,i):
    message =''
    form = add_sales_form()
    if request.method == 'POST':
        form = add_sales_form(request.POST)
        if form.is_valid():
            obj = article_sale()
            obj.article_id = form.cleaned_data['article_id']
            obj.selling_date = form.cleaned_data['selling_date']
            obj.cost_price = form.cleaned_data['cost_price']
            obj.selling_price = form.cleaned_data['selling_price']
            obj.customer_name = form.cleaned_data['customer_name']
            obj.save()
            return redirect('/home/')
        message =' Please enter valid values'
    return render(request,'add_sales.html',context={'form':form,'message':message})

def view_sales(request):
    obj = article_sale.objects.all()
    return render(request,'view_sales.html',context={'sales':obj})

@login_required
def delete_sales(request,i):
    obj = article_sale.objects.get(id=i)
    obj.delete()
    return redirect('/view_sales/')

@login_required
def edit_sales(request,i):
    obj = article_sale.objects.get(id=i)
    obj.article_id = request.POST['article_id']
    obj.selling_date = request.POST['selling_date']
    obj.cost_price = request.POST['cost_price']
    obj.selling_price = request.POST['selling_price']
    obj.customer_name = request.POST['customer_name']
    obj.save()
    return redirect('/view_sales/')
    
from django.shortcuts import render
from .models import ProductCategory, Product
# Create your views here.


def products(request):

    title = 'Каталог продукции'
    categories = ProductCategory.objects.all()
    products = Product.objects.all()[:4]

    context = {
        'title': title,
        'products': products,
        'categories': categories
    }

    return render(request, 'mainapp/products.html', context=context)

from django.shortcuts import render

# Create your views here.


def products(request):

    title = 'Каталог продукции'

    context = {
        'title': title,
    }

    return render(request, 'mainapp/products.html', context=context)

from django.shortcuts import render

# Create your views here.


def products(request):

    title = 'Каталог продукции'
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]

    context = {
        'title': title,
        'links': links_menu
    }

    return render(request, 'mainapp/products.html', context=context)

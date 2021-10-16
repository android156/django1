from django.shortcuts import render


def main(request):
    title = 'Главная страница. Магазин.'

    context = {
        'title': title,
    }
    return render(request, 'geekshop/index.html', context)

def contacts(request):
    title = 'Контакты'

    context = {
        'title': title,
    }
    return render(request, 'geekshop/contacts.html', context)





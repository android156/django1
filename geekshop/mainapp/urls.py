
from django.urls import path
from .views import products

urlpatterns = [
    path('', products),
]
# будем добавлять сюда новые пути для карточек продуктов
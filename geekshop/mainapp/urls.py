
from django.urls import path
from .views import products

urlpatterns = [
    path('', products, name='products'),
]
# будем активно добавлять сюда новые пути для карточек продуктов
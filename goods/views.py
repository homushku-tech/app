from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Product
def catalog(request):

    goods = Product.objects.all()

    context: dict[str, Any] ={
        'title': 'Home - Каталог',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context)
def product(request):
    return render(request, 'goods/product.html')

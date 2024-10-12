"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from main import views

#пространство имен
app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
"""
placeholder применяется от views к шаблону. Например {{title}} от request
jinja шаблонизатор или же django template {{ block css }} {{ endblock }} при наследовании шаблонов

Наследование шаблонов
создается базовый шаблон base.html
в дочерние шаблоны прописывается {%extends "main/base.html"%}
также есть {{ if условие }} {{ endif }} и {{ for }} {{ endfor }}
 
статика
{% load static %} везде где нужна статика
"{% static "deps/css/bootstrap/bootstrap.min.css" %}" пути к статике 
файлы статики в отдельной папке static в внутри приложения


urls в других приложениях 
копируем основной urls
оставляем нужные 
и прописываем пространство имен app_name = 'main'
также их прописываем в шаблонах  href="{% url "main:about" %}"



                                            django ORM и модели
в models.py делаем наши таблицы(сущности, классы)
вот пример:
class Categories(models.Model):
   name = models.CharField(max_length=150, unique=True)
   slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    class Meta:
        db_table = 'category'
делаем создание миграции командой makemigrations
и делаем миграции командой migrate
все наши миграции можно просмотреть в папке migrations
Мы можем всегда обратиться к админской панели через "{% url "admin" %}"
но чтобы зайти туда нужно создать суперпользователя командой python manage.py createsuperuser
далее чтобы наши модели отобразились в админпанели django их надо зарегистрировать в файле admin.py

django orm это и есть queryset и там свои определенные команды и с ними можно работать через shell
заходим python manage.py shell
обращаемся к конкретной модели from goods.models import Categories 
вводим запросы Categories.object.all или создаем новый объект Categories.object.create

                                        Примеры команды для django ORM
Product.objects.filter(price__lt=300).order_by('price') 
Product.objects.order_by('-price') 
Product.objects.filter(id = 2)
Product.objects.filter(price__lt=300) & Product.objects.filter(price__lt=100) 
Product.objects.filter(description__contains = 'диван') - аналогия LIKE в SQL
                                        Ленивые запросы (представления)
goods = Product.objects.filter(category_id=7).order_by('price') 
и вызываем только goods


модели в admin.py можно регистрировать вот так:
тут сделано с автогенерацией слагов
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
    
это позволяет их менять, но это еще малоизучено для меня.

 
Фикстуры
создание копию данных в бд в json-файл
создать сначало папку fixtures и в ней goods
для каждой модели прописываем команды
python manage.py dumpdata goods.Product > fixtures/goods/prod.json
python manage.py dumpdata goods.Categories > fixtures/goods/cats.json

debug_toolbar - мощный инструмент и считается как надстройка для django 
и его можно скачать и настроить
                                    Media
создаем папку media и проводим манипуляции в файле settings
Добавляем строки 
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

в файле urls - главный добавляем 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
                                     и
from django.conf.urls.static import static
from app import settings

далее обращаемся к ним. Например:
{% if product.image %}
        <img src="{{ product.image.url }}" class="card-img-top" alt="...">
{% else %}


                        templatetags
создаем папку templatetags внутри приложения, создаем внутри неё файл __init__.py
далее создаем файл, в котором создаем файл goods_tags.py  
содержимое файла:
from django import template
from goods.models import Categories

register = template.Library()
@register.simple_tag()
def tag_categories():
    return Categories.objects.all()
    
здесь мы создаем такой объект которым мы можем исползовать в html в обход контроллеров
и иметь доступ к данным к бд и использовать его везде
в html его мы подгружаем {% load goods_tags %}
и пользуемся им:
{% tag_categories as categories %}
                        {% for category in categories %}
                            <li><a class="dropdown-item text-white" href="{% url "goods:index" %}">{{ category.name }}</a></li>
                        {% endfor %}
"""
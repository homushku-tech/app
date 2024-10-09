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

модели в admin.py можно регистрировать вот так:
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
это позволяет их менять, но это еще малоизучено для меня.

 

"""
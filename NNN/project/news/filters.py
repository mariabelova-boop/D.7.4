from django_filters import FilterSet, DateTimeFilter
from .models import Post
from django.forms import DateTimeInput

class PostFilter(FilterSet):
    detail = DateTimeFilter(
        field_name = 'dateCreation',
        lookup_expr = 'gt',
        label = 'Дата публикации до:',
        widget = DateTimeInput(format='%Y-%m-%dT%H:%M',
                                attrs = {'type': 'datetime-local'} )

    )

    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по названию
           'title': ['icontains'],
           'categoryType': ['exact'],
           # количество товаров должно быть больше или равно
       }

class PostSearchFilter(FilterSet):
    detail = DateTimeFilter(
        field_name = 'dateCreation',
        lookup_expr = 'gt',
        label = 'Дата публикации до:',
        widget = DateTimeInput(format='%Y-%m-%dT%H:%M',
                                attrs = {'type': 'datetime-local'} )

    )

    class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по названию
           'title': ['icontains'],
           'categoryType': ['exact'],
           # количество товаров должно быть больше или равно
       }
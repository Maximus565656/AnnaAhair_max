from django.urls import path
from .views import index, catalog, contact, blog, my_works, review, online_entry


urlpatterns = [
    path('', index, name='index'),
    path('catalog', catalog, name='catalog'),
    path('contact', contact, name='contact'),
    path('blog', blog, name='blog'),
    path('my_works', my_works, name='my_works'),
    path('review', review, name='review'),
    path('online_entry', online_entry, name='online_entry'),

]

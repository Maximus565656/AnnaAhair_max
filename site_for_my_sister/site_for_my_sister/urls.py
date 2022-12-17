from django.contrib import admin
from django.urls import path, include
from annaahair import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('annaahair.urls')),

]

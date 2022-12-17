from django.contrib import admin
from .models import Annaahair, Annaahair_review

# Register your models here.
class AnnaahairAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'review']
    list_filter = ['title']
    list_display_links = ['title']
    search_fields = ['title']

class Annaahair_reviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'title1', 'review1']
    list_filter = ['title1']
    list_display_links = ['title1']
    search_fields = ['title1']


admin.site.register(Annaahair, AnnaahairAdmin)

admin.site.register(Annaahair_review, Annaahair_reviewAdmin)

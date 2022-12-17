from django.apps import AppConfig


class AnnaahairConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'annaahair'
    verbose_name = 'Блог'

class Annaahair_reviewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'annaahair_review'
    verbose_name = 'комментарий'

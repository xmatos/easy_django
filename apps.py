from django.apps import AppConfig
from . import views, models

class EasyConfig(AppConfig):
    name = 'easy_django'
    verbose_name = "Easy Django"

    def ready(self):
        for model in models.get_models():
            views.set_views(model)

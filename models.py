from django.conf import settings
from django.contrib.contenttypes.models import ContentType

def get_models():
    app_label = settings.EASY_DJANGO['apps'][0]
    models = ContentType.objects.filter(app_label=app_label)
    return models

from django import template
import easy_django.models


register = template.Library()


@register.assignment_tag
def get_models():
    models = easy_django.models.get_models()
    return models


@register.assignment_tag
def get_list_options(queryset):
    options = queryset.model._meta
    return options


@register.assignment_tag
def get_model_options(queryset):
    options = queryset._meta
    return options


@register.simple_tag
def get_field_value(obj, field):
    value = field.value_from_object(obj)
    return value

from django.conf.urls import url
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import urls

def set_views(model):
    model_name = model.model.capitalize()

    model_view = type(model_name + 'View', (), {
        'model': model.model_class()
    })

    list_view = type(model_name + 'List', (model_view, ListView), {
        'template_name': 'easy_django/model_list.html'
    })

    detail_view = type(model_name + 'Detail', (model_view, DetailView), {
        'template_name': 'easy_django/model_detail.html'
    })

    create_view = type(model_name + 'Create', (model_view, CreateView), {
        'success_url': reverse_lazy(model.model + '_list'),
        'template_name': 'easy_django/model_form.html'
    })

    update_view = type(model_name + 'Update', (model_view, UpdateView), {
        'success_url': reverse_lazy(model.model + '_list'),
        'template_name': 'easy_django/model_form.html'
    })

    delete_view = type(model_name + 'Delete', (model_view, DeleteView), {
        'success_url': reverse_lazy(model.model + '_list'),
        'template_name': 'easy_django/model_confirm_delete.html'
    })

    # /model
    urls.urlpatterns.append(url(r'^{}/$'.format(model.model),
                           list_view.as_view(),
                           name=(model.model + '_list')))

    # /model/{pk}
    urls.urlpatterns.append(url(r'^{}/(?P<pk>\d+)/$'.format(model.model),
                           detail_view.as_view(),
                           name=(model.model + '_detail')))

    # /model/add
    urls.urlpatterns.append(url(r'^{}/add/$'.format(model.model),
                           create_view.as_view(),
                           name=(model.model + '_add')))

    # /model/{pk}/edit
    urls.urlpatterns.append(url(r'^{}/(?P<pk>\d+)/edit/$'.format(model.model),
                           update_view.as_view(),
                           name=(model.model + '_edit')))

    # /model/{pk}/delete
    urls.urlpatterns.append(url(r'^{}/(?P<pk>\d+)/delete/$'.format(model.model),
                           delete_view.as_view(),
                           name=(model.model + '_delete')))

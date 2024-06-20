from django.urls import path

from webapp.views import index, add_cat, cat_actions

urlpatterns = [
    path('', index),
    path('add_cat/', add_cat),
    path('cat_actions/', cat_actions)
]

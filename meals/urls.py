from django.conf.urls import url
from .views import MealsListView


app_name = 'meals'
urlpatterns = [
    url(r'^$', MealsListView.as_view(), name='list'),
]

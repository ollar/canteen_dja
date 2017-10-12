from django.conf.urls import url
from .views import UsersListView


app_name = 'users'
urlpatterns = [
    url(r'^$', UsersListView.as_view(), name='list'),
]

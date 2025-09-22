from django.urls import path
from .views import home, test

app_name = 'forum'

urlpatterns = [
    path('home-page/', home, name='home_page'),
    path('test-page/', test, name='test_page')
]
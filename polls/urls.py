from django.conf.urls import url
from .views import base
from .views import sign_up
from .views import sign_in
from .views import location
from .views import order

urlpatterns = [

    url('index/', base, name='base_page'),
    url('signup/', sign_up, name='sign_up_page'),
    url('signin/', sign_in, name='sign_in_page'),
    url('location/', location, name='main location page'),
    url('order/', order, name='order result page'),
]
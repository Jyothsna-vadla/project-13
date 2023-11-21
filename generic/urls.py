from generic.views import *
from django.urls import path
app_name='generic'
urlpatterns=[
    path('jyo1/',jyo1,name='jyo1'),
    path('jyo2/',jyo2,name='jyo2'),
]
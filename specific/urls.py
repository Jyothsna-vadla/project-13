from specific.views import *
from django.urls import path
app_name='specific'
urlpatterns=[
    path('jyo3/',jyo3,name='jyo3'),
    path('jyo4/',jyo4,name='jyo4'),
]
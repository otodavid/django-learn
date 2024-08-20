from django.urls import path
from . import views
 
#create a list of url patterns
url_patterns = [
    path('', views.index)
] 
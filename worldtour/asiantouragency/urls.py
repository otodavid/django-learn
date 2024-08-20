from django.urls import path
from . import views
 
#create a list of url patterns
urlpatterns = [
    path('', views.index)
] 
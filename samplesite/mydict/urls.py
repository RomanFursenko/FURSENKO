from django.urls import path
from . import views

from .views import index

app_name = 'mydict'
urlpatterns = [
    path('mydict/', views.get_posts, name = 'posts'),
    path('', index, name = 'home')
]
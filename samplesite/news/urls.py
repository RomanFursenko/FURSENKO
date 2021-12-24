from django.contrib import admin
from django.urls import path, include

from news.views import index

urlpatterns = [
    path('', include('news.urls')),
    path('mydict/', include('mydict.urls')),
    path('admin/', admin.site.urls),

]

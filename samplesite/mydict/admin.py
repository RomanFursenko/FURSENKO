from django.contrib import admin
from .models import Md
from .models import *

class MdAdmin(admin.ModelAdmin):
    list_display = ('engword', 'rusword', 'content', 'published')
    list_display_links = ('engword', 'rusword')
    search_fields = ('engword', 'rusword', 'content')




admin.site.register(Md)
admin.site.register(Post)


# Register your models here.

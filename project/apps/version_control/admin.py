from django.contrib import admin
from .models import Repositorie, Environment, Tag, Client
# Register your models here.
admin.site.register(Repositorie)
admin.site.register(Environment)
admin.site.register(Tag)
admin.site.register(Client)
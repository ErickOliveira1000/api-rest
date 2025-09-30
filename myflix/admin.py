from django.contrib import admin
from myflix.models import User, Stream

# Register your models here.

class Users(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular')
    list_display_links = ('id', 'nome')
    list_per_page = 20
    search_fields = ['nome']



class Streams(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao')
    list_display_links = ('id', 'codigo')
    search_fields = ['codigo']


admin.site.register(User, Users)
admin.site.register(Stream, Streams)
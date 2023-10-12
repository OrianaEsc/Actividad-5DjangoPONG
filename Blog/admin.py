from django.contrib import admin
from Blog.models import Posteo, Categoria 

class PosteoAdmin(admin.ModelAdmin):
    pass
class CategoriaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Posteo, PosteoAdmin)
admin.site.register(Categoria, CategoriaAdmin)

# Register your models here.

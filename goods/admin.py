from django.contrib import admin
from .models import Category, Good


class CategoryAdmin(admin.ModelAdmin):
    pass

class GoodAdmin(admin.ModelAdmin):
    pass


         

admin.site.register(Category, CategoryAdmin)
admin.site.register(Good, GoodAdmin)


# Register your models here.

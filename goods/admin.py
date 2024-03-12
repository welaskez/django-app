from django.contrib import admin

from goods.models import Categoreis, Products

# admin.site.register(Categoreis)
# admin.site.register(Products)

@admin.register(Categoreis)
class CategoreisAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

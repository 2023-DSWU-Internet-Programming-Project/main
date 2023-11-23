from django.contrib import admin
from .models import *

admin.site.register(FindItem)
admin.site.register(AskItem)
admin.site.register(CompleteItem)
admin.site.register(Comment)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)

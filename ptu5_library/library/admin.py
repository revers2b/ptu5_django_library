from django.contrib import admin
from . import models
# Register your models here.

# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'display_genre')



admin.site.register(models.Author)
admin.site.register(models.Genre)
admin.site.register(models.Book)
admin.site.register(models.BookInstance)
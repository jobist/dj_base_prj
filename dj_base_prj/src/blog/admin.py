from django.contrib import admin

from blog.models import Article, Category
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'slug', )
    ordering = ['-id', 'name']


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['id', 'name', 'published', ]
    ordering = ['id', 'name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)

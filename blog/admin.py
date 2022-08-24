from django.contrib import admin
from . import models

admin.site.site_header = 'BurgerKing CMS Central'
admin.site.index_title = "The Admin"

# Register your models here.
@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','posted_date','post_img','author','slug','title']
    list_display_link = ['title','author','post_img']
    list_editable = ['title','author','post_img']




# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['id','posted_date','author','slug','title']


# admin.site.register(models.Article,ArticleAdmin)

from django.contrib import admin
from touch.models import Article, Product, News, Team, Question
# Register your models here.


class ArticleInline(admin.TabularInline):
    model = Article


class ProductInline(admin.TabularInline):
    model = Product


@admin.register(Product,News,Team,Question)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['label', 'article']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','date')  # list
    #inlines = [ProductInline ]
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )


admin.site.site_header = 'Touch管理系统'
admin.site.site_title = '后台管理'

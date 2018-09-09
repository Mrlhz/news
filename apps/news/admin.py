from django.contrib import admin

from .models import News, NewsCategory, HotSearchWords


# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    pass


class HotSearchWordsAdmin(admin.ModelAdmin):
    pass


class NewsCategoryAdmin(admin.ModelAdmin):
    pass


# admin.site.register(News, NewsAdmin)
# admin.site.register(HotSearchWords, HotSearchWordsAdmin)
# admin.site.register(NewsCategory, NewsCategoryAdmin)

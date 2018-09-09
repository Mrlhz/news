import xadmin

from .models import News, NewsCategory, HotSearchWords


class NewsAdmin(object):
    model_icon = 'fa fa-bolt'
    list_display = ['code', 'title', 'view_count', 'create_time']
    readonly_fields = ['view_count']
    # 搜索
    search_fields = ['title', 'content']
    # 过滤器
    list_filter = ['code']
    # 富文本
    # style_fields = {"detail": "ueditor"}
    style_fields = {"detail": "ueditor"}


class HotSearchWordsAdmin(object):
    model_icon = 'fa fa-h-square'


class NewsCategoryAdmin(object):
    model_icon = 'fa fa-bolt'


xadmin.site.register(News, NewsAdmin)
xadmin.site.register(HotSearchWords, HotSearchWordsAdmin)
xadmin.site.register(NewsCategory, NewsCategoryAdmin)

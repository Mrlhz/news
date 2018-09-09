from news.models import NewsCategory, News

from django.shortcuts import render
from django.views.generic import View


# Create your views here.


class NewsNavView(View):
    """
    新闻导航
    """

    def get(self, request):
        nav_display_lists = NewsCategory.objects.all().filter(is_tab=1)

        return render(request, 'index.html', {
            'nav_display_lists': nav_display_lists
        })

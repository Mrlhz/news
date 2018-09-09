from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.
class NewsCategory(models.Model):
    """
    新闻类别
    """
    name = models.CharField(default="", max_length=30, verbose_name="新闻类别", help_text="新闻类别")
    code = models.CharField(default="", max_length=30, verbose_name="类别code", help_text="类别code")
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "新闻类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class News(models.Model):
    code = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, null=True, verbose_name="新闻类型")
    title = models.CharField(default="", max_length=100, verbose_name="新闻标题")
    description = models.CharField(default="", max_length=500, verbose_name="简短描述")
    # content = models.TextField(default="", verbose_name="内容")
    content = UEditorField(verbose_name=u"内容", width=1000, height=300, imagePath="news/images/",
                           filePath="news/file/", default='')
    image = models.ImageField(upload_to="news/%Y/%m", null=True, blank=True, verbose_name="图片")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="修改时间")
    view_count = models.IntegerField(default=0, verbose_name="浏览次数")
    author_name = models.CharField(default="", max_length=100, verbose_name="FlashNews")

    class Meta:
        verbose_name = "新闻"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class HotSearchWords(models.Model):
    """
    热搜词
    """
    keywords = models.CharField(default="", max_length=20, verbose_name="热搜词")
    index = models.IntegerField(default=0, verbose_name="排序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '热搜词'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords

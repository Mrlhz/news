import xadmin
from xadmin import views

from users.models import EmailVerifyRecord, UserProfile


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "News管理系统"
    site_footer = "for study"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    model_icon = 'fa fa-envelope-o'


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

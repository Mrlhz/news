from django.shortcuts import render
from django.contrib.auth.backends import ModelBackend

from .models import UserProfile

from django.db.models import Q


# Create your views here.


# class CustomBackend(ModelBackend):
# def authenticate(self, username=None, password=None, is_staff=None, **kwargs):
#     try:
#         # 不希望用户存在两个，get只能有一个。两个是get失败的一种原因 Q为使用并集查询
#         user = UserProfile.objects.get(Q(username=username) | Q(email=username))
#         # django的后台中密码加密：所以不能password==password
#         # UserProfile继承的AbstractUser中有def check_password(self,
#         # raw_password):
#         if user.check_password(password):
#             if is_staff is not None:
#                 if user.is_staff == is_staff:
#                     return user
#                 else:
#                     return None
#             return user
#     except Exception as e:
#         return None


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 不希望用户存在两个，get只能有一个。两个是get失败的一种原因 Q为使用并集查询
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            # django的后台中密码加密：所以不能password==password
            # UserProfile继承的AbstractUser中有def check_password(self,
            # raw_password):
            if user.check_password(password):
                return user
        except Exception as e:
            return None

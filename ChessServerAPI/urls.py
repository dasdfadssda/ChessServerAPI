# urls.py

from django.urls import path
from .views import get_naver_token, get_naver_userinfo

urlpatterns = [
    path('naver/token/', get_naver_token, name='naver_token'),
    path('naver/userinfo/', get_naver_userinfo, name='naver_userinfo'),
]

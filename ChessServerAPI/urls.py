# urls.py

from django.urls import path
from .views import get_naver_token, get_naver_userinfo, default_endpoint

urlpatterns = [
    path('', default_endpoint, name='default_endpoint'),
    path('naver/token/', get_naver_token, name='naver_token'),
    path('naver/userinfo/', get_naver_userinfo, name='naver_userinfo'),
]


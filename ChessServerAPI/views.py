# views.py

import requests
from django.http import JsonResponse
from django.conf import settings
from django.http import HttpResponse

def default_endpoint(request):
    return HttpResponse(status=200)

def get_naver_token(request):
    code = request.GET.get('code')
    if not code:  # 'code' 값이 없으면 오류 메시지 출력
        print('code is missing')
        return JsonResponse({'error': 'code is missing'})

    state = request.GET.get('state')
    token_url = 'https://nid.naver.com/oauth2.0/token?'

    params = {
        'grant_type': 'authorization_code',
        'client_id': settings.NAVER_CLIENT_ID,
        'client_secret': settings.NAVER_SECRET_KEY,
        'redirect_uri': settings.NAVER_CALLBACK_URL,
        'code': code,
        'state': state,
    }

    response = requests.get(token_url, params=params)
    print(response.status_code)  # 응답 상태 코드 출력
    print(response.text)  # 응답 본문 출력

    access_token = response.json().get('access_token')
    if not access_token:  # 'access_token' 값이 없으면 오류 메시지 출력
        print('access_token is missing')
        return JsonResponse({'error': 'access_token is missing'})

    return JsonResponse({'access_token': access_token})

def get_naver_userinfo(request):
    access_token = request.GET.get('access_token')
    if not access_token:  # 'access_token' 값이 없으면 오류 메시지 출력
        print('access_token is missing')
        return JsonResponse({'error': 'access_token is missing'})

    profile_url = 'https://openapi.naver.com/v1/nid/me'

    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    response = requests.get(profile_url, headers=headers)
    print(response.status_code)  # 응답 상태 코드 출력
    print(response.text)  # 응답 본문 출력

    user_info = response.json().get('response')

    # user_info를 dict 형태로 변환
    user_info_dict = { 'user_info': user_info }

    # 이후 user_info_dict를 이용해 사용자를 생성하거나 업데이트합니다.

    return JsonResponse(user_info_dict)  # safe 매개변수를 False로 설정하지 않아도 됨


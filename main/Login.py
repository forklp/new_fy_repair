from django.shortcuts import HttpResponse, redirect
import json
import requests
from urllib import request
from urllib import parse
from urllib.request import urlopen
# Create your views here.
def login(request):
    if request.method == 'GET':
        try:
            uid = request.GET['uid']
            token = request.GET['token']
            appid = 1011
            appkey = 'jdf943u8uiefjwieu99e80we9'
            data = {
                "uid": uid,
                "token": token,
                "appid": appid,
                "appkey": appkey
            }
            url = 'https://sso.fyscu.com/api/challenge'
            r = requests.post(url, data=data)
            user_info = r.json()
            request.session['user_info'] = user_info
            return redirect('http://132.232.107.63:3000/dashboard')
        except:
            return HttpResponse('error')
    return HttpResponse('404')

def getUserInfo(request):
    if request.method == 'POST':
        if 'user_info' in request.session:
            data = request.session['user_info']
            return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse(404)

def logout(request):
    if request.method == 'POST':
        if 'user_info' in request.session:
            del request.session['user_info']
            return HttpResponse('success')
    return HttpResponse(404)



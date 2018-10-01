from django.shortcuts import HttpResponse, redirect
import json
# Create your views here.
def login(request):
    if request.method == 'GET':
        try:
            user_id = request.GET['uid']
            user_token = request.GET['token']
            request.session['uid'] = user_id
            request.sesssion['token'] = user_token
        except:
            pass
    return redirect('http://132.232.107.63:3000/dashboard')

def getUserInfo(request):
    if request.method == 'POST':
        appid = 1011
        appkey = 'jdf943u8uiefjwieu99e80we9'
        try:
            uid = request.session['uid']
            token = request.session['token']
        except:
            uid = ''
            token = ''
        data = {
            "uid": uid,
            "token": token,
            "appid": appid,
            "appkey": appkey
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse(404)

def logout(request):
    if request.method == 'POST':
        if 'uid' in request.session:
            del request.session['uid']
            del request.session['token']
            return HttpResponse('success')
    return HttpResponse(404)



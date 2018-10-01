from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request):
    if request.method == 'GET':
        user_id = request.GET['uid']
        return HttpResponse(user_id)

    return HttpResponse(0)
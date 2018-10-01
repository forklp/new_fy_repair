from django.shortcuts import HttpResponse, redirect
import json
from . import models


def getUser(request):
    if request.method == 'POST':
        pageSize = request.POST['pageSize']
        currentPage = request.POST['currentPage']
        ex_users = models.FyUserextend.objects.all()
        if 'name' in request.POST:
            name = request.POST['name']
            if ex_users.filter(name=name):
                ex_users = ex_users.filter(name=name)

        if 'phone' in request.POST:
            phone = request.POST['phone']
            if ex_users.filter(phone=phone):
                ex_users = ex_users.filter(phone=phone)

        users = []
        for ex_user in ex_users:
            type = models.FyUser.objects.get(user_id=ex_user.user_id).type
            email = -1
            status = -1
            if models.FyStaff.objects.filter(user_id=ex_user.user_id):
                email = models.FyStaff.objects.get(user_id=ex_user.user_id).email
                status = models.FyStaff.objects.get(user_id=ex_user.user_id).status
            user = {
                "id": ex_user.user_id,
                "type": type,
                "name": ex_user.name,
                "phone": ex_user.phone,
                "register_time": ex_user.register_time,
                "email": email,
                "status": status
            }
            users.append(user)

        if len(users) >= currentPage * pageSize:
            start = (currentPage - 1) * pageSize
            end = currentPage * pageSize
            new_users = users[start:end]
            total = pageSize
        else:
            start = (currentPage - 1) * pageSize
            new_users = users[start:]
            total = len(users) - start

        data = {
            "users": new_users,
            "total": total
        }

        return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse(404)


def modifyUser(request):
    if request.method == 'POST':
        user_id = request.POST['id']
        if 'type' in request.POST:
            type = request.POST['type']
            temp = models.FyUser.objects.get(user_id=user_id)
            temp.type = type
            temp.save()

        if 'status' in request.POST:
            status = request.POST['status']
            temp = models.FyStaff.objects.get(user_id=user_id)
            temp.status = status
            temp.save()

        return HttpResponse('success')
    return HttpResponse(404)

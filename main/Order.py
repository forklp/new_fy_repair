from django.shortcuts import HttpResponse, redirect
from . import models
import json


def getOrderList(request):
    if request.method == 'POST':
        currentPage = request.POST['currentPage']
        pageSize = request.POST['pageSize']
        users = models.FyUserextend.objects.all()
        if 'staffName' in request.POST:
            staffName = request.POST['staffName']
            if users.filter(name=staffName):
                users = users.filter(name=staffName)

        if 'userName' in request.POST:
            userName = request.POST['userName']
            if users.filter(name=userName):
                users = users.filter(name=userName)

        if 'userPhoneNumber' in request.POST:
            userPhoneNumber = request.POST['userPhoneNumber']
            if users.filter(phone=userPhoneNumber):
                users = users.filter(phone=userPhoneNumber)

        orders = []
        for user in users:
            if models.FyOrder.objects.filter(user_id=user.user_id):
                temp = models.FyOrder.objects.get(user_id=user.user_id)
                description = models.FyOrderextend.objects.get(order_id=temp.order_id).description
                user_id = models.FyStaff.objects.get(staff_id=temp.staff_id).user_id
                staffName = models.FyUserextend.objects.get(user_id=user_id).name
                userName = models.FyUserextend.objects.get(user_id=user.user_id).name
                phone = models.FyUserextend.objects.get(user_id=user.user_id).phone
                order = {
                    "order_id": temp.order_id,
                    "number": temp.number,
                    "staff_id": temp.staff_id,
                    "staff_name": staffName,
                    "user_id": temp.user_id,
                    "user_name": userName,
                    "user_phone_number": phone,
                    "time": temp.time,
                    "status": temp.status,
                    "vip": temp.vip,
                    "user_confirm_time": temp.user_confirm_time,
                    "staff_confirm_time": temp.staff_confirm_time,
                    "distribute_time": temp.distribute_time,
                    "computer_id": temp.computer_id,
                    "mode": temp.mode,
                    "description": description
                }
                orders.append(order)

            if models.FyStaff.objects.filter(user_id=user.user_id):
                staff_id = models.FyStaff.objects.get(user_id=user.user_id).staff_id
                if models.FyOrder.objects.filter(staff_id=staff_id):
                    temp = models.FyOrder.objects.get(staff_id=staff_id)
                    description = models.FyOrderextend.objects.get(order_id=temp.order_id).description
                    staffName = models.FyUserextend.objects.get(user_id=user.user_id).name
                    userName = models.FyUserextend.objects.get(user_id=temp.user_id).name
                    phone = models.FyUserextend.objects.get(user_id=temp.user_id).phone
                    order = {
                        "order_id": temp.order_id,
                        "number": temp.number,
                        "staff_id": temp.staff_id,
                        "staff_name": staffName,
                        "user_id": temp.user_id,
                        "user_name": userName,
                        "user_phone_number": phone,
                        "time": temp.time,
                        "status": temp.status,
                        "vip": temp.vip,
                        "user_confirm_time": temp.user_confirm_time,
                        "staff_confirm_time": temp.staff_confirm_time,
                        "distribute_time": temp.distribute_time,
                        "computer_id": temp.computer_id,
                        "mode": temp.mode,
                        "description": description
                    }
                    orders.append(order)

        if len(orders) >= currentPage * pageSize:
            start = (currentPage - 1) * pageSize
            end = currentPage * pageSize
            new_orders = orders[start:end]
            total = pageSize
        else:
            start = (currentPage - 1) * pageSize
            new_orders = orders[start:]
            total = len(orders) - start

        data = {
            "orders": new_orders,
            "total": total
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    return HttpResponse(404)


def reDistrubute(request):
    if request.method == 'POST':
        order_id = request.POST['orderId']
        if models.FyOrder.objects.filter(order_id=order_id):
            p = models.FyOrder.objects.get(order_id=order_id)
            p.status = 0
            p.save()
        return HttpResponse('success')
    return HttpResponse(404)

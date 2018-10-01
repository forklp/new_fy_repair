"""fy_repair URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import Login, Order, User
from main import tests


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/login', Login.login),
    path('login/info', Login.getUserInfo),
    path('login/logout', Login.logout),
    path('order', Order.getOrderList),
    path('order/redistrubute', Order.reDistrubute),
    path('user', User.getUser),
    path('user/modify', User.modifyUser),
    path('test/', tests.login)
]

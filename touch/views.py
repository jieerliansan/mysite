from django.shortcuts import render
from django.shortcuts import HttpResponse
from touch import models
# Create your views here.


def index(request):
    if request.method == "POST":
        username = request.POST.get("username", None);
        password = request.POST.get("password", None)
        u = models.UserInfo(user=username, pwd=password)
        u.save()
    #user_list = models.UserInfo.objects.all()
    #return HttpResponse("<p>数据添加成功！</p>")
    user_list = None
    return render(request, "index.html",{"data": user_list})
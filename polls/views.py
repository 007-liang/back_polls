from django.http import HttpResponse


# 相当于一个页面
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

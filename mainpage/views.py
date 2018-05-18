from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

# Create your views here.
def index(request):
    template = loader.get_template('mainpage/authpage.html')
    return HttpResponse(template.render())

def getUser(request):
    print(request.GET)

def clearRequest(request):
    # передать запрос как он есть
    print(request.get_full_path())
    return redirect('http://' + request.get_full_path()[1:])

# Запрос навсех друзей по id
# https://vk.com/dev/friends.get?params[user_id]=263728812&params[order]=name&params[count]=5&params[offset]=2&params[fields]=name&params[name_case]=nom&params[v]=5.75

# информация по пользователю
# http://warkb.pythonanywhere.com/dev/Login?uid=263728812&first_name=%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BCip%D1%8A&last_name=%D0%9A%D1%83%D1%80%D0%B1%D0%B0%D1%82%D0%BE%D0%B2%D1%8A&photo=https://pp.userapi.com/c629519/v629519812/b7ef/Qxdc1Jjz7b0.jpg&photo_rec=https://pp.userapi.com/c629519/v629519812/b7f2/qz4Pj1aONO0.jpg&hash=37587e7323e2e7c450d570ac0adc74e5
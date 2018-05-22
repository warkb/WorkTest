import json
import requests
from .models import User
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

app_id = '6481880'
app_secret = 'VgrTmwquRc6yaCCPiHc1'
cookie_name = 'warid'

token_request = 'https://oauth.vk.com/access_token?client_id=6481880&client_secret=VgrTmwquRc6yaCCPiHc1&redirect_uri=http://warkb.pythonanywhere.com/makeuser&code={code}'
profile_request = 'https://api.vk.com/method/users.get?user_ids={user_id}&v=5.75'
friends_request = 'https://api.vk.com/method/friends.get?user_id={user_id}&order=name&count=5&offset=2&fields=name&name_case=nom&v=5.75'

def sendRequestToApiVK(request, access_token):
    """отправляет запрос request к api vk, возвращает результат запроса"""
    response = requests.get(request + '&access_token=' + access_token + '&v=V')
    return response.json()['response']

def index(request):
    """стартовая страница"""
    if cookie_name in request.COOKIES:
        # пользователь есть
        # берем его id из cookie
        user_id = request.COOKIES.get(cookie_name)
        return HttpResponseRedirect('/userpage/%s' % user_id)
    # если дошли до этого момента, значит файла cookie нет
    # предлагаем авторизоваться через вк
    template = loader.get_template('mainpage/authpage.html')
    return HttpResponse(template.render())

def makeuser(request):
    """
    создает нового пользователя и перенаправляет на страницу пользователя
    """
    code = request.GET.get('code')
    responseVK = requests.get(token_request.format(code=code))
    json_response = responseVK.json()
    user_id = json_response['user_id']
    access_token = json_response['access_token']
    # делаем запрос к api вконтакте на имя человека и его друзей
    profileDict = sendRequestToApiVK(profile_request.format(user_id=user_id),
        access_token)[0]
    username = profileDict['first_name'] + ' ' + profileDict['last_name']
    friends = sendRequestToApiVK(friends_request.format(user_id=user_id),
        access_token)
    friendsCSV = ','.join([friend['last_name'] + ' ' +
        friend['first_name'] for friend in friends])
    # сохраняем пользователя в базе данных
    newUser = User(username=username, userid=user_id, token=access_token,
        friends=friendsCSV)
    newUser.save()
    # запоминаем id пользователя в куках
    response = HttpResponseRedirect('/userpage/%s' % user_id)
    response.set_cookie(cookie_name, user_id)
    return response

def userpage(request, userid):
    """отображает страницу пользователя"""
    user = list(User.objects.filter(userid=userid))[0]
    context = {
        'username': user.username,
        'friendlist': user.friends.split(',')
    }
    template = loader.get_template('mainpage/hello.html')
    return HttpResponse(template.render(context))

def clearRequest(request):
    # передать запрос как он есть
    print(request.get_full_path())
    return redirect('http://' + request.get_full_path()[1:])

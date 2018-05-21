import json
import requests
from .models import User
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

app_id = '6481880'
app_secret = 'VgrTmwquRc6yaCCPiHc1'

token_request = 'https://oauth.vk.com/access_token?client_id=6481880&client_secret=VgrTmwquRc6yaCCPiHc1&redirect_uri=http://warkb.pythonanywhere.com/makeuser&code={code}'
profile_request = 'https://api.vk.com/method/users.get?user_ids={user_id}&v=5.75'
friends_request = 'https://api.vk.com/method/friends.get?user_id={user_id}&order=name&count=5&offset=2&fields=name&name_case=nom&v=5.75'

def sendRequestToApiVK(request, access_token):
    """отправляет запрос request к api vk, возвращает результат запроса"""
    response = requests.get(request + '&access_token=' + access_token + '&v=V')
    return response.json()['response']

def index(request):
    template = loader.get_template('mainpage/authpage.html')
    return HttpResponse(template.render())

def makeuser(request):
    code = request.GET.get('code')
    response = requests.get(token_request.format(code=code))
    json_response = response.json()
    user_id = json_response['user_id']
    access_token = json_response['access_token']

    profileDict = sendRequestToApiVK(profile_request.format(user_id=user_id),
        access_token)[0]
    username = profileDict['first_name'] + ' ' + profileDict['last_name']
    friends = sendRequestToApiVK(friends_request.format(user_id=user_id),
        access_token)
    friendsCSV = ','.join([friend['last_name'] + ' ' +
        friend['first_name'] for friend in friends])

    newUser = User(username=username, userid=user_id, token=access_token,
        friends=friendsCSV)
    newUser.save()
    return HttpResponseRedirect('/userpage/%s' % user_id)

def userpage(request, userid):
    # magic
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

# Запрос на друзей по id

# https://api.vk.com/method/friends.get?user_id=263728812&order=name&count=5&offset=2&fields=name&name_case=nom&v=5.75&access_token=8c64f1b2ee1896c56b6e96bc61932957a24091ee0833cffa8b9681589e6486100fcbb29896995fe542dce&v=V

# getProf
# https://api.vk.com/method/users.get?user_ids=263728812&v=5.75&access_token=8c64f1b2ee1896c56b6e96bc61932957a24091ee0833cffa8b9681589e6486100fcbb29896995fe542dce&v=V
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from .models import UserInfo
from django.urls import reverse

def index(request):

    template = loader.get_template('index.html')

    return HttpResponse(template.render())

def check(request):
        if request.method != 'POST':
            
            template = loader.get_template('check.html')
            return HttpResponse(template.render({}, request))
        else:
            ui = UserInfo.objects.filter(UniqueId=request.POST['UniqueId']).exists()
            if ui ==True:
                patientdata = UserInfo.objects.get(UniqueId = request.POST['UniqueId'])
                template = loader.get_template('check.html')
                context = {
                'patientdata':patientdata,
                 }
                return HttpResponse(template.render(context, request))
            else:
                template = loader.get_template('check.html')
                context = {
                    'error': 'Data not found ! Register First .',
                    }
                return HttpResponse(template.render(context,request))


def register(request):
    template = loader.get_template('register.html')
    if request.method  =='POST':
        pasw = request.POST['password']
        retype = request.POST['retype']
        if pasw == retype:
            addrecord(request)
            return HttpResponseRedirect(reverse('index'))

        else:
            template = loader.get_template('register.html')
            context = {
            'passwordEr':'Password Mismatched !'
            }
            return HttpResponse(template.render(context,request))
    else:
        return HttpResponse(template.render({},request))

def addrecord(request):
    usernamef = request.POST['username']
    firstnamef = request.POST['firstname']
    lastnamef = request.POST['lastname']
    uniqueidf = request.POST['UniqueId']
    dobf = request.POST['dob']
    passwordf = request.POST['password']
    retypef = request.POST['retype']
    emailf = request.POST['email']
    userData = UserInfo(username = usernamef,email = emailf,password = passwordf,reType = retypef,firstname = firstnamef, lastname = lastnamef,UniqueId = uniqueidf,dob = dobf)
    userData.save()

from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you would like to contact me, plesae email me', 'test@test.com']})


def gallery(request):
    return render(request, 'personal/basicgallery.html')

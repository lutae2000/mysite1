from django.shortcuts import render
from django.http import HttpResponseRedirect
from guestbook.models import Guestbook
# Create your views here.

def index(request):
    guestbook_list = Guestbook.objects.all().order_by('-regdate')
    context = {'guestbook_list':guestbook_list}
    return render(request, 'guestbook/index.html', context)


def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.message = request.POST['message']

    guestbook.save()

    return HttpResponseRedirect('/guestbook')

def delete(request):
    # guestbook = Guestbook()
    # passwd = request.POST.get('password')
    # form_passwd =
    # if befor    e_id == passwd:
    #     guestbook.delete()
    # #delete from guestbook where form_passwd = passwd

    count = Guestbook.objects.filter(id=request.POST['id']).filter(password=request.POST['password']).count()

    if count != 0:
        Guestbook.objects.filter(id=request.POST['id']).filter(password=request.POST['password']).delete()
    # Guestbook.save()
    return HttpResponseRedirect('/guestbook')

def deleteform(request):
    id = request.GET.get('id')
    context = {'id': id}
    return render(request, 'guestbook/deleteform.html',context)
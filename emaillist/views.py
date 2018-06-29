from django.shortcuts import render
from django.http import HttpResponseRedirect
from emaillist.models import Emaillist

# Create your views here.


def index(request):
    emaillist_list = Emaillist.objects.all().order_by('-id')
    data = {'emaillist_list': emaillist_list}
    return render(request, 'emaillist/index.html', data)


def form(request):
    return render(request, 'emaillist/form.html')

def add(request):
    emaillist = Emaillist()
    emaillist.first_name = request.POST['fn']
    emaillist.last_name = request.POST['ln']
    emaillist.email = request.POST['email']

    emaillist.save()

    return HttpResponseRedirect('/emaillist')
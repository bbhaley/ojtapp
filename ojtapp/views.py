from django.shortcuts import render,get_object_or_404
from .models import Switch_set,Select
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template import loader
from . import forms
from .forms import LanForm


# Create your views here.

def menu(request):
	return render(request,"menu.html")
	
def dipsw(request):
	return render(request,"dip-sw.html")

def switch_set(request):

	return render(request,"switch_set.html")

def alm(request):
	return render(request,"alm.html")

def test(request, switch_id):
    switch =get_object_or_404(Switch_set,pk = switch_id)
    try:
        switch = Switch_set.objects.get(pk=switch_id)
    except Switch_set.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'test.html', {'switch': switch})

def new(request, switch_id):
    switch = get_object_or_404(Switch_set, pk=switch_id)
    return render(request, 'new_test.html', {'switch': switch})

def test2(request, switch_id):
    switch = get_object_or_404(Switch_set,pk =switch_id)
    try:
        selected = switch.select_set.get(pk=request.POST['select'])

    except (KeyError,Select.DoesNotExist):
        return render(request, 'test', {'switch': switch,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected.set = 1
        selected.save()
        return HttpResponseRedirect(reverse('new', args=(switch.id,)))

def Lan_set(request):
    d = {
        'form': forms.LanForm(),
    }
    return render(request, 'form_samples.html', d)


def test3(request):
    form = LanForm(request.POST)    
    args = {'form': form}
    return render(request,'form_samples.html', args)
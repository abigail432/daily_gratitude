from sqlite3 import Date
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .models import Graditude
from .forms import GratForm

# Create your views here.

def index(request):
    return HttpResponse("Welcome to daily gratitude!!")

def thanks(request):
    return HttpResponse("Thanks for submitting")

def dailyEntry(request):
    if request.method == 'POST':
        form = GratForm(request.POST)
        if form.is_valid():
            entry = form.cleaned_data['daily_entry']
                
            grat = Graditude()
            grat.date = Date.today()
            grat.gratitudes = entry
            grat.save()

            return HttpResponseRedirect('thanks/')
    else:
        form = GratForm()
    
    return render(request, 'dailyEntry.html', {'form': form})



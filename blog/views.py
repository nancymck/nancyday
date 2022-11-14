from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from datetime import datetime

# Create your views here.

def TodayView(request):

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    current_day = datetime.now()
    A = current_day.strftime('%A %-d')
    B = current_day.strftime('%B %Y')
    time = current_day.strftime('%H:%M')
    title = str()

    if current_day.day > 3:
        title = A+'th ' + B
    else:
        if current_day.day == 1:
            title = A+ 'st ' + B
        if current_day.day == 2:
            title = A+ 'nd ' + B
        if current_day.day == 3:
            title = A+ 'rd ' + B

    context = {'title': title, 'time': time}

    return render(request, 'today.html', context)

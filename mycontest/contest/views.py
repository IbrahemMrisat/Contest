# contest/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Contestant

def contest_entry(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')

        # Validate input
        if not (full_name and phone_number):
            return render(request, 'contest/entry.html', {'error': 'Please fill in all fields.'})

        # Save contestant
        contestant = Contestant(full_name=full_name, phone_number=phone_number)
        

        return render(request, 'contest/success.html')

    return render(request, 'contest/entry.html')

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from cycles.models import Cycle
from .models import Pickcycle
from django.contrib.auth.models import User
from django.utils import timezone

# Create your views here.

def pickcycle(request):
    allcycle = Cycle.objects.all()
    #allpickcycle = Pickcycle.objects.all()
    if request.method == 'POST':
        if request.POST['cycleid'] and request.POST['locationid']:
            pickcycle = Pickcycle()
            pickcycle.cycleid = request.POST['cycleid']
            pickcycle.locationid = request.POST
            ['locationid']
            pickcycle.Picker = request.user
            pickcycle.pick_date = timezone.datetime.now()
            pickcycle.save()
            #print(Picker)





    if request.method == 'POST':
        
        message = 'Cycle Id:' + request.POST['cycleid'] + ', Location Id:' + request.POST['locationid'] #+ ', Picker Name: ' + Pickcycle.objects.get(id = request.POST['cycleid'] ).Picker.username
        owner= Cycle.objects.get(id = request.POST['cycleid'] ).OwnerId.email
        send_mail('Pick Cycle',
        message,
        settings.EMAIL_HOST_USER,
        ['mrahman111213@gmail.com',owner],
        fail_silently=False
        )
    return render(request, 'pickcycles/pickcycle.html', {'allcycle':allcycle})



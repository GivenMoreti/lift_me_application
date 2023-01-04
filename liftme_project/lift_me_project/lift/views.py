from django.shortcuts import render
from . models import Lift
# Create your views here.
def index(request):

    lifts = Lift.objects.all()
    return render(request, 'lift/index.html', {'lifts':lifts})
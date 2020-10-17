from django.shortcuts import render
from .models import *

# Create your views here.



def event(request):

	return render(request, 'event/rtx.html')
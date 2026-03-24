from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Affirmation
import random

def affirmation_view(request):
    affirmations = Affirmation.objects.all()
    randomAffirmation = random.choice(affirmations) if affirmations else None
    template = loader.get_template('home.html')
    context ={
        'affirmation': randomAffirmation,
    }
    return HttpResponse(template.render(context, request))
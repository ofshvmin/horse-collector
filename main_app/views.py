from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Horse


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def horse_index(request):
  horses = Horse.objects.all()
  return render(request, 'horses/index.html', { 'horses': horses })

def horse_detail(request, horse_id):
  horse = Horse.objects.get(id=horse_id)
  return render(request, 'horses/detail.html', { 'horse': horse })

class HorseCreate(CreateView):
  model = Horse
  fields = '__all__'
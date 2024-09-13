from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Horse, Care
from .forms import FarrierApptForm


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
  farrier_appt_form = FarrierApptForm()
  return render(request, 'horses/detail.html', { 'horse': horse, 'farrier_appt_form': farrier_appt_form })

class HorseCreate(CreateView):
  model = Horse
  fields = '__all__'

class HorseUpdate(UpdateView):
  model = Horse
  fields = ['breed', 'description', 'age']

class HorseDelete(DeleteView):
  model = Horse
  success_url = '/horses/'

def add_farrierappt(request, horse_id):
  form = FarrierApptForm(request.POST)
  if form.is_valid():
    new_farrierappt = form.save(commit=False)
    new_farrierappt.horse_id = horse_id
    new_farrierappt.save()
  return redirect('horse-detail', horse_id=horse_id)

class CareCreate(CreateView):
  model = Care
  fields = '__all__'

class CareList(ListView):
  model = Care

class CareDetail(DeleteView):
  model = Care
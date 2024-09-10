from django.shortcuts import render
from django.http import HttpResponse
from .models import Horse


# horses = [
#   Horse('Tater Tot', 'Haflinger', 'A big potato who enjoys his job as a trail horse.', 21),
#   Horse('Aspen', 'Appaloosa', 'A demure southern lady with refined taste in riders.  Sorry folks, she is not for just anyone.  Aspen likes jumping and foxhunting best.', 14),
#   Horse('Morgan le Fay', 'Morgan/Percheron', 'A sweet girl just starting her career as an endurance champion.', 7)
# ]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def horse_index(request):
  horses = Horse.objects.all()
  return render(request, 'horses/index.html', { 'horses': horses })
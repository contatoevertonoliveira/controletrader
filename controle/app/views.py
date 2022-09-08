from django.shortcuts import render, redirect
from app.forms import EventosForm
from app.models import Eventos

# Create your views here.
def home(request):
  data = {}
  data['db'] = Eventos.objects.all()
  return render(request, 'index.html', data)

def form(request):
  data = {}
  data['form'] = EventosForm
  return render(request, 'form.html', data)

def create(request):
  form = EventosForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('home')
  
def view(request, pk):
  data = {}
  data['db'] = Eventos.objects.get(pk=pk)
  return render(request, 'view.html', data)
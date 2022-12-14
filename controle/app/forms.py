from dataclasses import fields
from django import forms
from django.forms import ModelForm
from app.models import Eventos

class EventosForm(forms.ModelForm):
  dataEvent = forms.DateField(widget=forms.DateInput(attrs={
    "class":"form-control",
    "placeholder":"00/00/0000"
  }))
  
  desc = forms.CharField(widget=forms.TextInput(attrs={
    "class":"form-control inputCustom",
    "placeholder":"Time Casa x Time Visitante"
  }))
  
  merc = forms.CharField(widget=forms.TextInput(attrs={
    "class":"form-control",
    "placeholder":"Probabilidades, Correct Score, Over Gols..."
  }))
  
  typeMerc = forms.CharField(widget=forms.TextInput(attrs={
    "class":"form-control",
    "placeholder":"À Favor, Contra..."
  }))
  
  odds = forms.CharField(widget=forms.TextInput(attrs={
    "class":"form-control",
    "placeholder":"1.50"
  }))
  
  invest = forms.FloatField(widget=forms.TextInput(attrs={
    "class":"form-control",
    "placeholder":"10.00"
  }))
  
  retor = forms.FloatField(widget=forms.TextInput(attrs={
    "class":"form-control",
    "placeholder":"5.00"
  }))
  
  pl1 = forms.IntegerField(widget=forms.TextInput(attrs={
    "class":"form-control",
    "placeholder":"3"
  }))
  
  pl2 = forms.IntegerField(widget=forms.TextInput(attrs={
    "class":"form-control",
    "placeholder":"2"
  }))
  
  statusTrader = forms.CharField(widget=forms.TextInput(attrs={
    "class":"form-control",
    "placeholder":"Em Andamento, Ganho ou Perdido"
  }))
  
  class Meta:
    model = Eventos
    fields = ['dataEvent','desc','merc','typeMerc','odds','invest','retor','pl1','pl2','statusTrader']
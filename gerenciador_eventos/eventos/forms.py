from django import forms
from .models import Evento, Participante

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'

class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = '__all__'

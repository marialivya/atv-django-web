from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento, Participante
from .forms import EventoForm, ParticipanteForm

def index(request):
    return render(request, 'index.html')

def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/listar_eventos.html', {'eventos': eventos})

def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = EventoForm()
    return render(request, 'eventos/criar_evento.html', {'form': form})

def detalhar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    return render(request, 'eventos/detalhar_evento.html', {'evento': evento})

def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/editar_evento.html', {'form': form})

def excluir_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('listar_eventos')
    return render(request, 'eventos/excluir_evento.html', {'evento': evento})

def listar_participantes(request):
    participantes = Participante.objects.all()
    return render(request, 'participantes/listar_participantes.html', {'participantes': participantes})

def criar_participante(request):
    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_participantes')
    else:
        form = ParticipanteForm()
    return render(request, 'participantes/criar_participante.html', {'form': form})

def editar_participante(request, pk):
    participante = get_object_or_404(Participante, pk=pk)
    if request.method == 'POST':
        form = ParticipanteForm(request.POST, instance=participante)
        if form.is_valid():
            form.save()
            return redirect('listar_participantes')
    else:
        form = ParticipanteForm(instance=participante)
    return render(request, 'participantes/editar_participante.html', {'form': form})

def excluir_participante(request, pk):
    participante = get_object_or_404(Participante, pk=pk)
    if request.method == 'POST':
        participante.delete()
        return redirect('listar_participantes')
    return render(request, 'participantes/excluir_participante.html', {'participante': participante})

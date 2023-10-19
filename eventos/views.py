from django.shortcuts import render, redirect
from .models import Evento, RegistroEvento, Usuario
from .forms import EventoForm, RegistroEventoForm, RegistroUsuarioForm, EventoUpdateForm, RegistroEventoUpdateForm

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'eventos/registrar_usuario.html', {'form': form})

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'eventos/crear_evento.html', {'form': form})

def detalle_evento(request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    registros = RegistroEvento.objects.filter(evento=evento)
    return render(request, 'eventos/detalle_evento.html', {'evento': evento, 'registros': registros})

def editar_evento(request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('detalle_evento', evento_id=evento_id)
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/editar_evento.html', {'form': form, 'evento': evento})

def eliminar_evento(request, evento_id):
    evento = Evento.objects.get(pk=evento_id)
    evento.delete()
    return redirect('lista_eventos')

def registrar_evento(request):
    if request.method == 'POST':
        form = RegistroEventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = RegistroEventoForm()
    
    return render(request, 'eventos/registrar_evento.html', {'form': form})

def editar_registro_evento(request, registro_id):
    registro = RegistroEvento.objects.get(pk=registro_id)
    if request.method == 'POST':
        form = RegistroEventoForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('detalle_evento', evento_id=registro.evento.id)
    else:
        form = RegistroEventoForm(instance=registro)
    return render(request, 'eventos/editar_registro_evento.html', {'form': form, 'registro': registro})

def eliminar_registro_evento(request, registro_id):
    registro = RegistroEvento.objects.get(pk=registro_id)
    evento_id = registro.evento.id
    registro.delete()
    return redirect('detalle_evento', evento_id=evento_id)
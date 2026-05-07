from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import Calificacion
from .forms import CalificacionForm, RegistroForm


class CustomLoginView(LoginView):
    template_name = 'calificaciones/login.html'
    redirect_authenticated_user = True


def registro(request):
    if request.user.is_authenticated:
        return redirect('listar_calificaciones')
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('listar_calificaciones')
    else:
        form = RegistroForm()
    return render(request, 'calificaciones/registro.html', {'form': form})


@login_required
def crear_calificacion(request):
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_calificaciones')
    else:
        form = CalificacionForm()
    return render(request, 'calificaciones/crear.html', {'form': form})


@login_required
def listar_calificaciones(request):
    calificaciones = Calificacion.objects.all()
    promedio_general = calificaciones.aggregate(Avg('promedio'))['promedio__avg']
    return render(request, 'calificaciones/listar.html', {
        'calificaciones': calificaciones,
        'promedio_general': promedio_general
    })


@login_required
def editar_calificacion(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            return redirect('listar_calificaciones')
    else:
        form = CalificacionForm(instance=calificacion)
    return render(request, 'calificaciones/editar.html', {'form': form, 'calificacion': calificacion})


@login_required
def eliminar_calificacion(request, pk):
    calificacion = get_object_or_404(Calificacion, pk=pk)
    if request.method == 'POST':
        calificacion.delete()
        return redirect('listar_calificaciones')
    return render(request, 'calificaciones/eliminar.html', {'calificacion': calificacion})

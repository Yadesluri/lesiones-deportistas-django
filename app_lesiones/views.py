from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Estudiante, Lesion, Tratamiento
from .forms import EstudianteForm, LesionForm, TratamientoForm
from django.contrib import messages
from django.http import JsonResponse
import requests



def requiere_entrenador(request):
    if not request.user.groups.filter(name='Entrenadores').exists():
        messages.error(request, "No tienes permiso para realizar esta acción.")
        return False
    return True


# ============================
# VALIDADORES DE ROLES
# ============================
def es_entrenador(user):
    return user.groups.filter(name='Entrenadores').exists()

def es_kinesio(user):
    return user.groups.filter(name='Kinesiologos').exists()


# ============================
# PANEL DE INICIO
# ============================
@login_required
def panel_inicio(request):
    if request.user.groups.filter(name='Entrenadores').exists():
        return redirect('panel_entrenador')

    if request.user.groups.filter(name='Kinesiologos').exists():
        return redirect('panel_kinesio')

    messages.error(request, "Tu usuario no tiene un rol asignado.")
    return redirect('logout')


# ============================
# HOME GENERAL
# ============================
def inicio(request):
    return render(request, 'app_lesiones/inicio.html')


# ============================
# PANEL ENTRENADOR / KINESIO
# ============================
@login_required
@user_passes_test(es_entrenador)
def panel_entrenador(request):
    return render(request, 'app_lesiones/panel_entrenador.html')


@login_required
@user_passes_test(es_kinesio)
def panel_kinesio(request):
    return render(request, 'app_lesiones/panel_kinesio.html')


# ============================
# CRUD ESTUDIANTES
# ============================
@login_required
@user_passes_test(es_entrenador)
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'app_lesiones/estudiantes_lista.html', {'estudiantes': estudiantes})


@login_required
@user_passes_test(es_entrenador)
def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Estudiante creado correctamente.")
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm()

    return render(request, 'app_lesiones/formulario.html', {
        'form': form,
        'titulo': 'Nuevo Estudiante',
        'volver': 'lista_estudiantes'
    })


@login_required
@user_passes_test(es_entrenador)
def editar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)

    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            messages.success(request, "Estudiante actualizado.")
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)

    return render(request, 'app_lesiones/formulario.html', {
        'form': form,
        'titulo': 'Editar Estudiante',
        'volver': 'lista_estudiantes'
    })


@login_required
@user_passes_test(es_entrenador)
def eliminar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    estudiante.delete()
    messages.success(request, "Estudiante eliminado correctamente.")
    return redirect('lista_estudiantes')


# ============================
# CRUD LESIONES
# ============================
@login_required
@user_passes_test(lambda u: u.groups.filter(name__in=['Entrenadores','Kinesiologos']).exists())
def lista_lesiones(request):
    lesiones = Lesion.objects.all()
    return render(request, 'app_lesiones/lesiones_lista.html', {'lesiones': lesiones})

    lesiones = Lesion.objects.all()
    return render(request, 'app_lesiones/lesiones_lista.html', {'lesiones': lesiones})


@login_required
def crear_lesion(request):

    if not requiere_entrenador(request):
        return redirect('lista_lesiones')

    if request.method == 'POST':
        form = LesionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_lesiones')
    else:
        form = LesionForm()

    return render(request, 'app_lesiones/lesiones_form.html', {
        'form': form,
        'titulo': 'Nueva Lesión',
        'volver': 'lista_lesiones'
    })


@login_required
def editar_lesion(request, id):

    if not requiere_entrenador(request):
        return redirect('lista_lesiones')

    lesion = get_object_or_404(Lesion, id=id)

    if request.method == 'POST':
        form = LesionForm(request.POST, instance=lesion)
        if form.is_valid():
            form.save()
            return redirect('lista_lesiones')
    else:
        form = LesionForm(instance=lesion)

    return render(request, 'app_lesiones/lesiones_form.html', {
        'form': form,
        'titulo': 'Editar Lesión',
        'volver': 'lista_lesiones'
    })


@login_required
def eliminar_lesion(request, id):

    if not requiere_entrenador(request):
        return redirect('lista_lesiones')

    lesion = get_object_or_404(Lesion, id=id)
    lesion.delete()
    return redirect('lista_lesiones')

# ============================
# CRUD TRATAMIENTOS
# ============================
@login_required
@user_passes_test(es_kinesio)
def lista_tratamientos(request):
    tratamientos = Tratamiento.objects.all()
    return render(request, 'app_lesiones/tratamientos_lista.html', {'tratamientos': tratamientos})


@login_required
@user_passes_test(es_kinesio)
def crear_tratamiento(request):
    if request.method == 'POST':
        form = TratamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tratamientos')
    else:
        form = TratamientoForm()

    return render(request, 'app_lesiones/tratamientos_form.html', {
        'form': form,
        'titulo': 'Nuevo Tratamiento',
        'volver': 'lista_tratamientos'
    })


@login_required
@user_passes_test(es_kinesio)
def editar_tratamiento(request, id):
    tratamiento = get_object_or_404(Tratamiento, id=id)

    if request.method == 'POST':
        form = TratamientoForm(request.POST, instance=tratamiento)
        if form.is_valid():
            form.save()
            return redirect('lista_tratamientos')
    else:
        form = TratamientoForm(instance=tratamiento)

    return render(request, 'app_lesiones/tratamientos_form.html', {
        'form': form,
        'titulo': 'Editar Tratamiento',
        'volver': 'lista_tratamientos'
    })


@login_required
@user_passes_test(es_kinesio)
def eliminar_tratamiento(request, id):
    tratamiento = get_object_or_404(Tratamiento, id=id)
    tratamiento.delete()
    return redirect('lista_tratamientos')


# ============================
# API REST - LESIONES (JSON)
# ============================

from django.http import JsonResponse

def api_lesiones(request):
    lesiones = Lesion.objects.all().values(
        'id',
        'tipo',
        'descripcion',
        'fecha',
        'estudiante_id'
    )
    return JsonResponse(list(lesiones), safe=False)

# ============================
# API EXTERNA - CLIMA (OPEN-METEO)
# ============================

def api_clima(request):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=-33.45&longitude=-70.66"
        "&current_weather=true"
    )

    response = requests.get(url)
    data = response.json()

    return JsonResponse(data, safe=False)

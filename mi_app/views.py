from django.shortcuts import render
from django.contrib.auth import logout as auth_logout
from django.http import JsonResponse
from .models import CitaMedica
import json

def home(request):
    if request.method == 'POST':
        try:
            datos = json.loads(request.body)
            # 1. Si la petición es para guardar el RUT en la sesión (Login simple)
            if "login_rut" in datos:
                request.session["rut_usuario"] = datos["login_rut"].strip()
                return JsonResponse({"status": "ok"})

            # 2. Si la petición es para crear una nueva cita médica
            if "nombre" in datos:
                CitaMedica.objects.create(
                    paciente=datos['nombre'],
                    rut=datos['rut'],
                    especialidad=datos['especialidad'],
                    fecha_hora=datos['fecha_hora']
                )
                return JsonResponse({'status': 'ok'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    citas = CitaMedica.objects.all().order_by("fecha_hora")

    rut_buscado = request.session.get("rut_usuario", "")

    if rut_buscado:
        citas = citas.filter(rut=rut_buscado)
    else:
        citas = citas.none()

    contexto = {
        'nombre_pagina': 'HoraContigo',
        'eslogan': 'Simplificamos tu cita, cuidamos de ti.',
        "citas": citas,
        "rut_buscado": rut_buscado
    }
    return render(request, 'home.html', contexto)

def logout_view(request):
  auth_logout(request)
  if request.headers.get('x-requested-with') == 'XMLHttpRequest' or (
      request.method == 'POST'
  ):
    return JsonResponse({'status': 'ok'})
  return redirect('home')

def api_disponibilidad(request):
    citas = CitaMedica.objects.all()
    eventos = []
    for cita in citas:
        eventos.append({
            'title': 'Ocupado 🚫',
            'start': cita.fecha_hora.isoformat(),
            'color': '#E53E3E'
        })
    return JsonResponse(eventos, safe=False)

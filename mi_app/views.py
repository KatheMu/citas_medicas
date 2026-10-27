from django.shortcuts import render
from django.http import JsonResponse
from .models import CitaMedica
import json

def home(request):
    if request.method == 'POST':
        try:
            datos = json.loads(request.body)
            CitaMedica.objects.create(
                paciente=datos['nombre'],
                rut=datos['rut'],
                especialidad=datos['especialidad'],
                fecha_hora=datos['fecha_hora']
            )
            return JsonResponse({'status': 'ok'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    contexto = {
        'nombre_pagina': 'HoraContigo',
        'eslogan': 'Simplificamos tu cita, cuidamos de ti.',
    }
    return render(request, 'home.html', contexto)

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

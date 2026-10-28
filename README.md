# HoraContigo – Citas Médicas

> *Simplificamos tu cita, cuidamos de ti.*

HoraContigo es una aplicación web hecha con **Django** para agendar citas médicas de forma simple, pensada para personas que necesitan una interfaz clara y con pocos pasos (por ejemplo, adultos mayores).

## Funcionalidades

- Asistente de reserva en 3 pasos:
  1. Ingreso de nombre y RUT del paciente.
  2. Selección de especialidad (Medicina General, Cardiología, Geriatría / Adulto Mayor).
  3. Resumen de la cita.
- Modelo `CitaMedica` para guardar paciente, RUT, especialidad y fecha/hora.
- Endpoint `GET /api/disponibilidad/` que devuelve las horas ya ocupadas en formato JSON (compatible con calendarios tipo FullCalendar).
- Endpoint `POST /` que recibe una cita en JSON y la guarda en la base de datos.

## Estado del proyecto

En desarrollo. Pendiente:

- [ ] Selector de fecha y hora en el asistente.
- [ ] Conectar el paso final con el servidor (hoy solo muestra un mensaje de confirmación).
- [ ] Mostrar las horas ocupadas usando `/api/disponibilidad/`.
- [ ] Validar RUT, fechas pasadas y citas duplicadas.
- [ ] Registrar el modelo en el panel de administración.

## Tecnologías

- Python 3
- Django (proyecto generado con Django 6.1.2)
- SQLite
- HTML, CSS y JavaScript

## Estructura

```
citas_medicas/
├── manage.py
├── mi_sitio/          # Configuración del proyecto (settings, urls)
└── mi_app/            # Aplicación principal
    ├── models.py      # Modelo CitaMedica
    ├── views.py       # Vista home y API de disponibilidad
    └── templates/
        └── home.html  # Interfaz del asistente de reserva
```

## Instalación y uso

1. Clona el repositorio:

   ```bash
   git clone https://github.com/KatheMu/citas_medicas.git
   cd citas_medicas
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate      # En Windows: venv\Scripts\activate
   ```

3. Instala Django:

   ```bash
   pip install django
   ```

4. Crea la base de datos:

   ```bash
   python manage.py migrate
   ```

5. (Opcional) Crea un usuario administrador:

   ```bash
   python manage.py createsuperuser
   ```

6. Inicia el servidor:

   ```bash
   python manage.py runserver
   ```

7. Abre http://127.0.0.1:8000/ en tu navegador.

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/` | Página principal con el asistente de reserva |
| POST | `/` | Crea una cita (JSON: `nombre`, `rut`, `especialidad`, `fecha_hora`) |
| GET | `/api/disponibilidad/` | Lista de horas ocupadas |
| GET | `/admin/` | Panel de administración de Django |

## Aviso

Este proyecto maneja datos personales (nombre y RUT). No subas la base de datos (`db.sqlite3`) ni claves secretas al repositorio, y configura `SECRET_KEY`, `DEBUG` y `ALLOWED_HOSTS` de forma segura antes de publicarlo.

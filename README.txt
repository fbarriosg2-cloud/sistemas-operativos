SITIO WEB: SISTEMAS OPERATIVOS (Flask)

1. Instala Python 3.10 o superior.
2. Abre CMD/Terminal en esta carpeta.
3. Crea entorno virtual:
   Windows: py -m venv .venv
   Windows: .venv\Scripts\activate
   Linux/macOS: python3 -m venv .venv && source .venv/bin/activate
4. Instala dependencias:
   pip install -r requirements.txt
5. Ejecuta:
   python app.py
6. Abre en el navegador:
   http://127.0.0.1:5000

ESTRUCTURA:
app.py                 Backend Flask y rutas API
banker.py              Lógica del algoritmo del banquero
templates/index.html    Frontend HTML + JavaScript
static/style.css       Diseño responsive

SIMULADOR:
- Disponible: vector de recursos libres.
- Asignación: recursos actualmente asignados a cada proceso.
- Necesidad: recursos máximos restantes que cada proceso requiere.
- El endpoint /api/banker verifica secuencia segura.
- /api/banker/request evalúa una petición provisional y la concede solo si conserva estado seguro.

IMPORTANTE:
Este es un prototipo educativo local. Para publicarlo en Internet, configura un servidor WSGI
(por ejemplo Gunicorn), variables de entorno, HTTPS y validación robusta de entradas.
Para subirlo como enlace público puedes desplegarlo en Render, PythonAnywhere u otro hosting
compatible con Flask. El servidor local 127.0.0.1 no genera un enlace público.

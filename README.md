# Simulador del Algoritmo del Banquero

Aplicación educativa construida con Flask para comprobar estados seguros y evaluar solicitudes provisionales de recursos.

## Ejecutar localmente (Windows)

```bat
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Visita http://127.0.0.1:5000

## Publicar

1. Sube esta carpeta a un repositorio GitHub.
2. En Render, crea un Web Service y conecta el repositorio.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`

También se incluye `render.yaml` para configuración Blueprint.

## API

- `POST /api/banker`: recibe `available`, `allocation`, `maximum`.
- `POST /api/banker/request`: además recibe `process` (índice desde 0) y `request`.

Prototipo académico; valida los datos, pero no sustituye controles de seguridad de producción.

from flask import Flask, render_template, request, jsonify
from banker import safe_sequence, request_resources

app = Flask(__name__)

CONTENIDOS = [
    {"titulo":"Orígenes y evolución temprana de la tecnología","texto":"La tecnología comenzó con herramientas simples para resolver necesidades humanas. Con la agricultura, la escritura, la imprenta, la electricidad y la electrónica, la sociedad desarrolló sistemas cada vez más complejos."},
    {"titulo":"Breve historia de los sistemas operativos","texto":"Los primeros computadores trabajaban sin sistemas operativos. Después aparecieron procesamiento por lotes, multiprogramación, tiempo compartido, sistemas personales, redes, móviles y plataformas en la nube."},
    {"titulo":"Evolución de los sistemas operativos","texto":"La evolución pasó de ejecución manual y por lotes a sistemas multitarea, multiusuario, distribuidos, virtualizados y orientados a servicios."},
    {"titulo":"Hardware y software de la computadora","texto":"Hardware: CPU, RAM, almacenamiento, placa base y periféricos. Software: sistema operativo, controladores, aplicaciones y utilidades."},
    {"titulo":"Ecosistema del sistema operativo","texto":"Incluye kernel, controladores, servicios, bibliotecas, interfaz, aplicaciones, usuarios, dispositivos y herramientas de administración."},
    {"titulo":"Componentes del sistema operativo","texto":"Kernel, administrador de procesos, memoria, archivos, entrada/salida, seguridad, red, interfaz y llamadas al sistema."},
    {"titulo":"Algoritmo del banquero","texto":"El algoritmo de seguridad de Dijkstra comprueba si existe una secuencia de procesos que pueda terminar con los recursos disponibles, evitando conceder asignaciones que dejen al sistema en un estado inseguro."},
    {"titulo":"Hilos","texto":"Un hilo es una unidad de ejecución dentro de un proceso. Los hilos de un mismo proceso comparten memoria y recursos, pero mantienen su propio contador de programa y pila."},
    {"titulo":"Procesos","texto":"Un proceso es un programa en ejecución con estado, espacio de memoria y recursos. El sistema operativo crea, planifica, suspende y finaliza procesos."},
    {"titulo":"Comentario personal","texto":"Considero que los sistemas operativos son fundamentales porque coordinan el hardware y el software, permiten ejecutar aplicaciones y ofrecen seguridad y facilidad de uso. Comprender procesos, hilos y memoria ayuda a diseñar programas eficientes."},
    {"titulo":"Comparación de sistemas operativos para servidor","texto":"Linux Server suele destacar por flexibilidad, automatización y variedad de distribuciones. Windows Server ofrece integración con herramientas Microsoft y administración gráfica. Unix y BSD son reconocidos por estabilidad y diseño robusto. La elección depende del costo, soporte, seguridad, aplicaciones y experiencia del equipo."}
]

@app.route("/")
def index():
    return render_template("index.html", contenidos=CONTENIDOS)

@app.post("/api/banker")
def api_banker():
    data = request.get_json(force=True)
    result = safe_sequence(data["available"], data["allocation"], data["need"])
    return jsonify(result)

@app.post("/api/banker/request")
def api_request():
    data = request.get_json(force=True)
    result = request_resources(data["available"], data["allocation"], data["need"],
                               data["request"], data["process"])
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

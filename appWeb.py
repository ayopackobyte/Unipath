from flask import Flask, render_template, request, redirect, url_for

from gestor import Gestor


app = Flask(__name__)

gestor = Gestor()


facultad_actual = "Facultad de Ingeniería y Arquitectura"

gestor.seleccionar_carrera("Ingenieria en Sistemas")

carga_actual = []
mensaje = ""


@app.route("/")
def index():

    total_creditos = sum(m.creditos for m in carga_actual)

    catalogo = []

    for codigo in gestor.materias:

        m = gestor.materias[codigo]

        cadena = gestor.grafo.contar_cadena(codigo)
        aprobada = codigo in gestor.aprobadas

        catalogo.append({
            "codigo": m.codigo,
            "nombre": m.nombre,
            "creditos": m.creditos,
            "semestre": m.semestre,
            "cadena": cadena,
            "aprobada": aprobada
        })

    return render_template(
        "index.html",

        facultades=list(gestor.facultades.keys()),
        facultad_actual=facultad_actual,

        carreras=gestor.facultades[facultad_actual],
        carrera_actual=gestor.carrera_actual,

        catalogo=catalogo,
        carga_actual=carga_actual,
        total_creditos=total_creditos,
        mensaje=mensaje
    )


@app.route("/cambiar_facultad", methods=["POST"])
def cambiar_facultad():

    global facultad_actual, mensaje

    facultad = request.form.get("facultad")

    if facultad in gestor.facultades:

        facultad_actual = facultad

        carreras = gestor.facultades[facultad]

        if carreras:
            gestor.seleccionar_carrera(carreras[0])
            carga_actual.clear()

        mensaje = f"Facultad cambiada a {facultad}."

    return redirect(url_for("index"))


@app.route("/cambiar_carrera", methods=["POST"])
def cambiar_carrera():

    global mensaje

    carrera = request.form.get("carrera")

    if carrera in gestor.facultades[facultad_actual]:

        if gestor.seleccionar_carrera(carrera):

            carga_actual.clear()
            mensaje = f"Carrera cambiada a {carrera}."

    return redirect(url_for("index"))


@app.route("/agregar/<codigo>")
def agregar(codigo):

    global mensaje

    if codigo in gestor.aprobadas:
        mensaje = f"Aviso: Ya aprobaste {codigo}."
        return redirect(url_for("index"))

    for m in carga_actual:

        if m.codigo == codigo:
            mensaje = f"Aviso: {codigo} ya esta en tu proyeccion."
            return redirect(url_for("index"))

    if codigo not in gestor.materias:
        return redirect(url_for("index"))

    ok, faltantes = gestor.grafo.puede_matricular(
        codigo, gestor.aprobadas
    )

    if not ok:
        mensaje = f"Bloqueo por Grafo: Te falta aprobar {', '.join(faltantes)}."
        return redirect(url_for("index"))

    materia = gestor.materias[codigo]

    total = sum(m.creditos for m in carga_actual)

    if total + materia.creditos > 18:
        mensaje = "Error: Excedes el limite de 18 creditos."
        return redirect(url_for("index"))

    carga_actual.append(materia)

    mensaje = f"Exito: {materia.nombre} agregada a tu carga."

    return redirect(url_for("index"))


@app.route("/quitar/<codigo>")
def quitar(codigo):

    global mensaje

    for m in carga_actual:

        if m.codigo == codigo:

            carga_actual.remove(m)
            mensaje = f"Materia {codigo} quitada de la proyeccion."
            break

    return redirect(url_for("index"))


@app.route("/aprobar/<codigo>")
def aprobar(codigo):

    global mensaje

    if codigo in gestor.aprobadas:
        mensaje = f"Aviso: {codigo} ya estaba aprobada."
        return redirect(url_for("index"))

    ok, faltantes = gestor.grafo.puede_matricular(
        codigo, gestor.aprobadas
    )

    if not ok:
        mensaje = f"Bloqueo: No puedes aprobar {codigo} sin antes aprobar {', '.join(faltantes)}."
        return redirect(url_for("index"))

    gestor.aprobadas.append(codigo)

    for m in carga_actual:

        if m.codigo == codigo:
            carga_actual.remove(m)
            break

    mensaje = f"Exito: {codigo} marcada como APROBADA."

    return redirect(url_for("index"))


@app.route("/recomendar", methods=["POST"])
def recomendar():

    global mensaje

    try:

        promedio = float(request.form.get("promedio", ""))

        if promedio < 0 or promedio > 100:
            mensaje = "Error: El promedio debe estar entre 0 y 100."
            return redirect(url_for("index"))

        recomendadas, max_cred = gestor.recomendar_carga(promedio)

        carga_actual.clear()

        for m in recomendadas:
            carga_actual.append(m)

        mensaje = f"Simulacion lista (Promedio {promedio}): Limite de {max_cred} creditos."

    except ValueError:
        mensaje = "Error: Ingresa un numero valido para el promedio."

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

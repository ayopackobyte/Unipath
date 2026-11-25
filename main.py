from gestor import Gestor

gestor = Gestor()
carga_actual = []

def elegir_carrera():
    nombres = list(gestor.carreras.keys())
    if len(nombres) == 0:
        print("Error: No hay carreras registradas en el sistema.")
        return
    while True:
        print("\n---SELECCIONA UNA CARRERA---")
        for i in range(len(nombres)):
            print(f"{i + 1}. {nombres[i]}")
        try:
            entrada = input("Elige el numero de carrera: ").strip()
            if entrada == "":
                print("Error: Debes ingresar un numero.")
                continue

            opcion = int(entrada)
            if opcion < 1 or opcion > len(nombres):
                print(f"Error: Elige una opcion entre 1 y {len(nombres)}.")
                continue

            carrera_elegida = nombres[opcion - 1]
            gestor.seleccionar_carrera(carrera_elegida)
            carga_actual.clear()
            print(f"\nCarrera cargada: {gestor.carrera_actual}")
            break
        except ValueError:
            print("Error: Dato invalido. Por favor ingresa solo el numero (ej. 1).")

def ver_catalogo():
    print("\n--- CATALOGO DE MATERIAS ---")
    for m in gestor.arbol.recorrido_inorden():
        cadena = gestor.grafo.contar_cadena(m.codigo)
        
        estado = "Pendiente"
        if m.codigo in gestor.aprobadas:
            estado = "APROBADA"
            
        print(f"{m.codigo} | {m.nombre} | Creditos: {m.creditos} | Sem: {m.semestre} | Cadena: {cadena} | {estado}")
def ver_carga():
    print("\n--- MI PROYECCION DE MATRICULA ---")
    if len(carga_actual) == 0:
        print("No tienes materias agregadas.")
        return

    total = 0
    for m in carga_actual:
        print(f"- {m.codigo}: {m.nombre} ({m.creditos} creditos)")
        total += m.creditos
    print(f"Total de creditos: {total} / 18")

def agregar_materia():
    codigo = input("Escribe el codigo de la materia: ").upper().strip()
    
    materia = gestor.arbol.buscar(codigo)
    if materia is None:
        print("Esa materia no existe.")
        return
    
    if codigo in gestor.aprobadas:
        print("Ya aprobaste esa materia.")
        return

    for m in carga_actual:
        if m.codigo == codigo:
            print("Ya esta en tu proyeccion.")
            return

    ok, faltantes = gestor.grafo.puede_matricular(codigo, gestor.aprobadas)
    if not ok:
        print("No puedes llevarla. Te falta aprobar:", faltantes)
        return

    
    total = 0
    for m in carga_actual:
        total += m.creditos

    if total + materia.creditos > 18:
        print("Te pasas del limite de 18 creditos.")
        return

    carga_actual.append(materia)
    print("Materia agregada correctamente.")

def quitar_materia():
    codigo = input("Codigo de la materia a quitar: ").upper().strip()
    for m in carga_actual:
        if m.codigo == codigo:
            carga_actual.remove(m)
            print("Materia eliminada de tu carga.")
            return
    print("No tienes esa materia en tu carga.")

def aprobar_materia():
    codigo = input("Codigo de la materia aprobada: ").upper().strip()
    
    if gestor.arbol.buscar(codigo) is None:
        print("Ese codigo no existe.")
        return

    if codigo in gestor.aprobadas:
        print("Ya estaba aprobada.")
        return

    ok, faltantes = gestor.grafo.puede_matricular(codigo, gestor.aprobadas)
    if not ok:
        print("No puedes aprobarla sin antes aprobar:", faltantes)
        return

    gestor.aprobadas.append(codigo)
    
    for m in carga_actual:
        if m.codigo == codigo:
            carga_actual.remove(m)
            break

    print("Materia marcada como aprobada.")
    ver_catalogo()

def buscar_materia():
    codigo = input("Escribe el codigo de la materia a buscar: ").upper().strip()
    materia = gestor.arbol.buscar(codigo)
    if materia is None:
        print("No se encontro esa materia en el arbol.")
    else:
        print(f"Encontrada: {materia.codigo} - {materia.nombre} | Creditos: {materia.creditos} | Semestre: {materia.semestre}")

def simular_recomendacion():
    try:
        promedio = float(input("Ingresa tu promedio (0 a 100): "))
    except ValueError:
        print("Error: Ingresa un numero valido.")
        return

    recomendadas, max_cred = gestor.recomendar_carga(promedio)
    
    carga_actual.clear()
    for m in recomendadas:
        carga_actual.append(m)

    print(f"\nLimite de creditos segun tu promedio: {max_cred}")
    print("Materias sugeridas cargadas a tu proyeccion:")
    ver_carga()

elegir_carrera()

while True:
    print("\n SIMULACIÓN DE ESTRUCTURAS DE DATOS")
    print("1. Ver catalogo de materias")
    print("2. Ver mi proyeccion de matricula")
    print("3. Agregar materia a mi carga")
    print("4. Quitar materia de mi carga")
    print("5. Marcar materia como aprobada")
    print("6. Simular recomendacion de carga")
    print("7. Cambiar de carrera")
    print("8. Buscar materia por codigo")
    print("0. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        ver_catalogo()
    elif opcion == "2":
        ver_carga()
    elif opcion == "3":
        agregar_materia()
    elif opcion == "4":
        quitar_materia()
    elif opcion == "5":
        aprobar_materia()
    elif opcion == "6":
        simular_recomendacion()
    elif opcion == "7":
        elegir_carrera()
    elif opcion == "8":
        buscar_materia()
    elif opcion == "0":
        print("Programa terminado.")
        break
    else:
        print("Opcion incorrecta.")

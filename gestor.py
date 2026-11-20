from modelos import Asignatura
from grafo import Grafo

class Gestor:
    def __init__(self):
        self.carreras = {}
        self.carrera_actual = ""
        self.materias = {}
        self.grafo = Grafo()
        self.aprobadas = []
        self.cargar_datos_iniciales()
        
    def cargar_datos_iniciales(self):
        materias_sistemas = {}
        grafo_sistemas = Grafo()
        lista_sistemas = [
                Asignatura("SIS101", "Introduccion a Sistemas", 3, 1),
                Asignatura("MAT101", "Calculo I", 4, 1),
                Asignatura("PRG101", "Programacion Estructurada", 4, 1),
                Asignatura("MAT102", "Calculo II", 4, 2),
                Asignatura("PRG102", "Estructuras de Datos", 4, 2),
                Asignatura("FIS101", "Fisica I", 4, 2),
                Asignatura("BD101", "Bases de Datos I", 3, 3),
                Asignatura("RED101", "Redes I", 4, 3),
                Asignatura("IA101", "Inteligencia Artificial", 3, 4)
            ]

        for m in lista_sistemas:
            materias_sistemas[m.codigo] = m
            grafo_sistemas.agregar_materia(m.codigo)

        
            grafo_sistemas.agregar_relacion("MAT101", "MAT102")
            grafo_sistemas.agregar_relacion("PRG101", "PRG102")
            grafo_sistemas.agregar_relacion("MAT101", "FIS101")
            grafo_sistemas.agregar_relacion("PRG102", "BD101")
            grafo_sistemas.agregar_relacion("FIS101", "RED101")
            grafo_sistemas.agregar_relacion("PRG102", "IA101")
            grafo_sistemas.agregar_relacion("BD101", "IA101")
        
        self.carreras["Ingenieria en Sistemas"] = {
            "materias": materias_sistemas,
            "grafo": grafo_sistemas
        }

        #ewes te paso la estructura de datos que estoy usando para guardar las materias y el grafo de cada carrera. 
        """materias = {}
        grafos = Grafo()
        lista = ["""

        self.seleccionar_carrera("Ingenieria en Sistemas")
        #Esto se puede borrar mas adelante.

    def seleccionar_carrera(self, nombre_carrera):
        if nombre_carrera not in self.carreras:
            return False
        self.carrera_actual = nombre_carrera
        self.materias = self.carreras[nombre_carrera]["materias"]
        self.grafo = self.carreras[nombre_carrera]["grafo"]
        self.aprobadas = []
        return True

    def recomendar_carga(self, promedio):
        if promedio < 0 or promedio > 100:
            return [], 0

        if promedio >= 80:
            max_creditos = 18
        else:
            max_creditos = 14

        disponibles = []
        for codigo in self.materias:
            if codigo not in self.aprobadas:
                ok, _ = self.grafo.puede_matricular(codigo, self.aprobadas)
                if ok:
                    materia = self.materias[codigo]
                    importancia = self.grafo.contar_cadena(codigo)
                    disponibles.append((importancia, materia))

        
        n = len(disponibles)
        for i in range(n):
            for j in range(0, n - i - 1):
                if disponibles[j][0] < disponibles[j + 1][0]:
                    temp = disponibles[j]
                    disponibles[j] = disponibles[j + 1]
                    disponibles[j + 1] = temp

        recomendadas = []
        creditos_totales = 0
        for importancia, materia in disponibles:
            if creditos_totales + materia.creditos <= max_creditos:
                recomendadas.append(materia)
                creditos_totales += materia.creditos

        return recomendadas, max_creditos
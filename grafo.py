class Grafo:
    def __init__(self):
        self.siguientes = {} 
        self.prerrequisitos = {}

    def agregar_materia(self, codigo):
        if codigo == "":
            return
        if codigo not in self.siguientes:
            self.siguientes[codigo] = []
        if codigo not in self.prerrequisitos:
            self.prerrequisitos[codigo] = []

    def agregar_relacion(self, materia_antes, materia_despues):
        if materia_antes == materia_despues:
            print("Error: Una materia no puede ser prerrequisito de si misma.")
            return
        
        self.agregar_materia(materia_antes)
        self.agregar_materia(materia_despues)

        if materia_despues not in self.siguientes[materia_antes]:
            self.siguientes[materia_antes].append(materia_despues)
        if materia_antes not in self.prerrequisitos[materia_despues]:
            self.prerrequisitos[materia_despues].append(materia_antes)
        
    def puede_matricular(self, codigo, aprobadas):
        faltantes = []
        for req in self.prerrequisitos[codigo]:
           if req not in aprobadas:
                faltantes.append(req)

        return len(faltantes) == 0, faltantes
        
    def contar_cadena(self, codigo, visitados= None):
        if codigo not in self.siguientes:
            return 0
        if visitados is None:
            visitados = set()
        if codigo in visitados:
            return 0

        visitados.add(codigo)
        mayor = 0
        for sig in self.siguientes[codigo]:
            cantidad = self.contar_cadena(sig, visitados.copy())
            if cantidad > mayor:
                mayor = cantidad
        return 1 + mayor

class Asignatura:
    def __init__(self, codigo, nombre, creditos, semestre):
        if codigo.strip() == "" or nombre.strip() == "":
            raise ValueError("El codigo y el nombre no pueden estar vacios.")
        if creditos <= 0 or semestre <= 0:
            raise ValueError("Los creditos y el semestre deben ser mayores a 0.")

        self.codigo = codigo.upper().strip()
        self.nombre = nombre.strip()
        self.creditos = int(creditos)
        self.semestre = int(semestre)
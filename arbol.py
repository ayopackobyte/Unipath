class NodoArbol:

    def __init__(self, materia):
        self.materia = materia
        self.izq = None
        self.der = None


class ArbolMaterias:

    def __init__(self):
        self.raiz = None

    def insertar(self, materia):

        nuevo = NodoArbol(materia)

        if self.raiz is None:
            self.raiz = nuevo
            return

        actual = self.raiz

        while True:

            if materia.codigo < actual.materia.codigo:

                if actual.izq is None:
                    actual.izq = nuevo
                    break

                actual = actual.izq

            elif materia.codigo > actual.materia.codigo:

                if actual.der is None:
                    actual.der = nuevo
                    break

                actual = actual.der

            else:
                break

    def buscar(self, codigo):

        actual = self.raiz

        while actual is not None:

            if codigo == actual.materia.codigo:
                return actual.materia

            elif codigo < actual.materia.codigo:
                actual = actual.izq

            else:
                actual = actual.der

        return None

    def recorrido_inorden(self):

        lista = []
        self._inorden(self.raiz, lista)
        return lista

    def _inorden(self, nodo, lista):

        if nodo is not None:
            self._inorden(nodo.izq, lista)
            lista.append(nodo.materia)
            self._inorden(nodo.der, lista)

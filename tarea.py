class Tarea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.listo = False

    def terminar(self):
        self.listo = True

    def obtenerNombre(self):
        return self.nombre

    def estaLista(self):
        return self.listo
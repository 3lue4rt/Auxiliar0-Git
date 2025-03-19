class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.tareas = []

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)

    def listarTareas(self):
        for tarea in self.tareas:
            if tarea.estaLista():
                print(f"[X] {tarea.obtenerNombre()}" )
<<<<<<< HEAD
                print("Duarte")
=======
                print("Gabriel")
>>>>>>> 7aea21a6cf798cb5cc392e159079fcb5cd48911d

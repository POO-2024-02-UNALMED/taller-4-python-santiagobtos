from classroom.asignatura import Asignatura

class Grupo:
    grado = "grado 12"

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None  ):
        self._grupo = grupo
        self.asignaturas = asignaturas if asignaturas is not None else []
        self.listadoAlumnos = estudiantes if estudiantes is not None else []

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None: 
            lista = []
        lista.append(alumno)
        for elemento in lista:
            if elemento not in self.listadoAlumnos:
                self.listadoAlumnos.append(elemento)

    def __str__(self):
        if self._grupo== "grupo ordinado":
            cadena= "Grupo de estudiantes: grupo predeterminado"
            return cadena
        else :
            cadena="Grupo de estudiantes: "+ self._grupo
            return cadena

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

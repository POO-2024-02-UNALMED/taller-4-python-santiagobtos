from classroom.asignatura import Asignatura

class Grupo:
    grado = "grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=[]):
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self):
        if self._grupo== "grupo predeterminado":
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

class Asignatura:

    def __init__(self, nombre, salon="remoto"):
        self._nombre = nombre
        self._salon = salon

    def __str__(self):
        if self._salon=="remoto":
            cadena=self._nombre+" remoto"
            return cadena
        else:
            cadena=self._nombre+" "+self._salon
            return cadena

class Asignatura:

    def __init__(self, nombre, salon=None):
        self._nombre = nombre
        self._salon = salon

    def __str__(self):
        if self._salon==None:
            cadena=self._nombre+" Remoto"
            return cadena
        else:
            cadena=self._nombre+" "+self._salon
            return cadena

class Mascota:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def info(self):
        return f"Soy una mascota llamada {self.nombre}"
    
class Perro(Mascota):
    def info(self):
        return f"{self.nombre} (Perro)"
    
class Gato(Mascota):
    def info(self):
        return f"{self.nombre} (Gato)"
    

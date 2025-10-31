class Tamagotchi:
    def __init__(self, nombre, color, salud=100, felicidad=100, energia=100):
        self.nombre = nombre
        self.color = color
        self.salud = salud
        self.felicidad = felicidad
        self.energia = energia

    def jugar(self):
        self.felicidad += 10
        self.salud -= 5

    
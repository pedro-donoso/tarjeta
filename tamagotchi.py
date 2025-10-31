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


    def comer(self):
        self.felicidad += 5
        self.salud += 10


    def curar(self):
        self.salud += 20
        self.felicidad -= 5



class Persona:
    def __init__(self, nombre, apellido, tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi


    def jugar_con_tamagotchi(self):
        self.tamagotchi.jugar()


    def darle_comida(self):
        self.tamagotchi.comer()


    def curarlo(self):
        self.tamagotchi.curar()

mi_tamagotchi = Tamagotchi('Pipo', 'azul')

persona = Persona('Maria', 'González', mi_tamagotchi)

persona.darle_comida()
persona.curarlo()
persona.jugar_con_tamagotchi()

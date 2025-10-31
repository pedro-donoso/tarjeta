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
        print(f"{self.nombre} jugó! Felicidad: {self.felicidad}, Salud: {self.salud}")

    def comer(self):
        self.felicidad += 5
        self.salud += 10
        print(f"{self.nombre} comió! Felicidad: {self.felicidad}, Salud: {self.salud}")
        
    def curar(self):
        self.salud += 20
        self.felicidad -= 5
        print(f"{self.nombre} fue curado! Felicidad: {self.felicidad}, Salud: {self.salud}")


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
print(f"Nació {mi_tamagotchi.nombre}! Color: {mi_tamagotchi.color}")
print(f"Estado inicial - Salud: {mi_tamagotchi.salud}, Felicidad: {mi_tamagotchi.felicidad}, Energia: {mi_tamagotchi.energia}\n")

persona = Persona('Maria', 'González', mi_tamagotchi)
print(f"{persona.nombre} {persona.apellido} adoptó a {mi_tamagotchi.nombre}!\n")

print("--- Interacciones ---")
persona.darle_comida()
persona.curarlo()
persona.jugar_con_tamagotchi()

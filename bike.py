import datetime

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class BikeCityError(Exception):
    pass


class Bicicleta:
    def __init__(self, id_bicicleta, modelo, precio_hora):
        self.id_bicicleta = id_bicicleta
        self.modelo = modelo
        self.precio_hora = precio_hora
        self.estado = 'disponible'  


class Reserva:
    def __init__(self, id_reserva, bicicleta, cliente, horas):
        self.id_reserva = id_reserva
        self.bicicleta = bicicleta
        self.cliente = cliente
        self.horas = horas
        self.estado = "activa"
        self.monto = bicicleta.precio_hora * horas



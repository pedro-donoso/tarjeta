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
        self.estado = 'activa'
        self.monto = bicicleta.precio_hora * horas


class SistemaBIKECITY:
    def __init__(self):
        self.bicicletas = {}
        self.reservas = {}
        self.proximo_id = 1

    def registrar_bicicleta(self, id_bici, modelo, precio):
        try:
            if id_bici in self.bicicletas:
                raise BikeCityError("Bicicleta ya existe")
            self.bicicletas[id_bici] = Bicicleta(id_bici, modelo, precio)
            logging.info(f"Bicicleta {id_bici} registrada")
        except Exception as e:
            logging.error(f"Error: {e}")
            raise

    
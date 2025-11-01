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

    def crear_reserva(self, id_bici, cliente, horas):
        try:
            if horas <= 0 or horas > 24:
                raise BikeCityError("Horas inválidas")
            
            if id_bici not in self.bicicletas:
                raise BikeCityError("Bicicleta no encontrada")
            
            bici = self.bicicletas[id_bici]
            if bici.estado != "disponible":
                raise BikeCityError("Bicicleta no disponible")
            
            for r in self.reservas.values():
                if r.bicicleta.id_bicicleta == id_bici and r.estado == "activa":
                    raise BikeCityError("Ya existe reserva activa")
                
            reserva = Reserva(self.proximo_id, bici, cliente, horas)
            self.reservas[self.proximo_id] = reserva
            bici.estado = 'reservada'
            self.proximo_id += 1
            logging.info(f"Reserva {reserva.id_reserva} creada")
            return reserva
        
        except Exception as e:
            logging.error(f"Error en reserva: {e}")
            raise


    def iniciar_uso(self, id_reserva):
        try:
            reserva = self.reservas.get(id_reserva)
            if not reserva:
                raise BikeCityError("Reserva no encontrada")
            reserva.bicicleta.estado = 'en_uso'
            reserva.estado = 'en_uso'
            logging.info(f"Uso iniciado reserva {id_reserva}")
        except Exception as e:
            logging.error(f"Error: {e}")
            raise

    
    def finalizar_uso(self, id_reserva, km):
        try:
            reserva = self.reservas.get(id_reserva)
            if not reserva or reserva.estado != "en_uso":
                raise BikeCityError("No se puede finalizar")
            

            reserva.bicicleta.estado = 'disponible'
            reserva.estado = 'completada'
            logging.info(f"Uso finalizado: ${reserva.monto}, {km}km")
            return reserva.monto
        

        except Exception as e:
            logging.error(f"Error: {e}")
            raise
        finally:
            print("Operación completada")


    def obtener_disponibles(self):
        return [b for b in self.bicicletas.values() if b.estado == 'disponible']
    

    def reporte(self):
        print("\n=== REPORTE BIKECITY ===")
        print(f"Bicicletas: {len(self.bicicletas)}")
        print(f"Disponibles: {len(self.obtener_disponibles())}")
        for b in self.bicicletas.values():
            print(f" {b.id_bicicleta} - {b.modelo} - {b.estado}")


def demo():
    sistema = SistemaBIKECITY()
    try:
        sistema.registrar_bicicleta('B001', 'Montaña', 5)
        sistema.registrar_bicicleta('B002', 'Urbana', 4)

        reserva = sistema.crear_reserva('B001', 'Juan', 2)
        sistema.iniciar_uso(reserva.id_reserva)
        monto = sistema.finalizar_uso(reserva.id_reserva, 10)
        print(f"Monto: ${monto}")


        sistema.reporte()


    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Demo finalizada")


if __name__ == "__main__":
    demo()

















    
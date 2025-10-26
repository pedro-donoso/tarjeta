class TarjetaCredito:
    def __init__(self, saldo_pagar=0, limite_credito=5000, intereses=0.02):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses

    def compra(self, monto):
        credito_disponible = self.limite_credito - self.saldo_pagar

        if monto <= credito_disponible:
            self.saldo_pagar += monto
            print(f"Compra de ${monto:.2f} realizada. Saldo a pagar: ${self.saldo_pagar:.2f}")
        else:
            print(f"Compra rechazada. Crédito disponible: ${credito_disponible:.2f}")

        return self
    
    def pago(self, monto):
        if monto <= self.saldo_pagar:
            self.saldo_pagar -= monto
            print(f"Pago de ${monto:.2f} realizado. Saldo restante: ${self.saldo_pagar:.2f}")
        else:
            print(f"El monto excede el saldo a pagar. Saldo actual: ${self.saldo_pagar}")

        return self

    def mostrar_info_tarjeta(self):
        credito_disponible = self.limite_credito - self.saldo_pagar
        print("=" * 40)
        print("INFORMACIÓN DE TARJETA DE CRÉDITO")
        print("=" * 40)
        print(f"Límite de crédito: ${self.limite_credito:.2f}")
        print(f"Saldo a pagar: ${self.saldo_pagar:.2f}")
        print(f"Crédito disponible: ${credito_disponible:.2f}")
        print(f"Tasa de interés: {self.interes * 100:.2f}%")
        print("=" * 40)

        return self
    
    def cobrar_interes(self):
        if self.saldo_pagar > 0:
            interes_cobrado = self.saldo_pagar * self.intereses
            self.saldo_pagar += interes_cobrado
            print(f"Interés cobrado: ${interes_cobrado:.2f}. Nuevo saldo: ${self.saldo_pagar:.2f}")
        else:
            print("No hay saldo pendiente. No se cobra intereses.")   

        return self
    
print("CREANDO TARJETAS...\n")
tarjeta1 = TarjetaCredito(limite_credito=3000, intereses=0.025)
tarjeta2 = TarjetaCredito(limite_credito=5000, intereses=0.02)
tarjeta3 = TarjetaCredito(limite_credito=2000, intereses=0.03)

print("\n--- TARJETA 1 ---")
tarjeta1.compra(800).compra(500).pago(300).cobrar_interes().mostrar_info_tarjeta()

print("\n--- TARJETA 2 ---")
tarjeta2.compra(1000).compra(800).compra(800).pago(600).pago(500).pago(400).cobrar_interes().mostrar_info_tarjeta()

print("\n--- TARJETA 3 ---")
tarjeta3.compra(400).compra(600).compra(500).compra(800).compra(300).mostrar_info_tarjeta()
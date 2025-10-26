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
    
    

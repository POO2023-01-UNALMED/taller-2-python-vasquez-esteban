
class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        counter = 0

        for asiento in self.asientos:
            if type(asiento) == Asiento:
                counter += 1
        return counter

    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
        else:
            for asiento in self.asientos:
                if type(asiento) != Asiento:
                    continue
                else:
                    if asiento.registro != self.motor.registro:
                        return "Las piezas no son originales"
                    return "Auto original"


class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color == "rojo":
            self.color = "rojo"
        if color == "verde":
            self.color = "verde"
        if color == "amarillo":
            self.color = "amarillo"
        if color == "negro":
            self.color = "negro"
        if color == "blanco":
            self.color = "blanco"


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo == "electrico":
            self.tipo = "electrico"
        elif tipo == "gasolina":
            self.tipo = "gasolina"


if __name__ == "__main__":
    a1 = Auto("model 3", 33000, [Asiento("blanco", 5000, 32), None, None, Asiento("blanco", 5000, 32), None],
              "tesla", Motor(4, "electrico", 32), 32)
    a2 = Auto("model 3", 33000, [Asiento("blanco", 5000, 40), None, None, Asiento("blanco", 5000, 32), None],
              "tesla", Motor(4, "electrico", 32), 32)

    print(a1.verificarIntegridad())
    print(a2.verificarIntegridad())


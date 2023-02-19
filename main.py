
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
        return len(self.asientos)

    def verificarIntegridad(self):
        if self.motor.registro == self.registro:
            for asiento in self.asientos:
                if asiento.registro != self.registro:
                    return "Las piezas no son originales"
                else:
                    continue
            return "Auto original"
        return "Las piezas no son originales"


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

class Carro:

  def __init__(self):
    self.marca = ""
    self.modelo = ""
    self.cor = ""
    self.capacidadeTanque = 0
    self.kmPorLitro = 0

  def calcularAutonomia(self):
    return self.capacidadeTanque * self.kmPorLitro

  def calcularCombustivel(self, km):
    return km / self.kmPorLitro
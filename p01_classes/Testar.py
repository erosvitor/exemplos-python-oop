#!python3

import Carro

carro1 = Carro.Carro()
carro1.marca = "Ford"
carro1.modelo = "Fusion"
carro1.cor = "Preta"
carro1.capacidadeTanque = 55
carro1.kmPorLitro = 8

autonomia = carro1.calcularAutonomia()
print(f"Autonomia do carro {carro1.modelo} é de {autonomia}")

quilometragem = 400
qtdeCombustivel = carro1.calcularCombustivel(quilometragem)
print(f"Para uma viagem de {quilometragem}km, são necessários {qtdeCombustivel} litros de combustível")
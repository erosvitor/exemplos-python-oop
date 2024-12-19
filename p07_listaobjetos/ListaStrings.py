#!python3

# Criando uma lista vazia para strings
peixes = []

# Adicionando valores
peixes.append("Robalo")
peixes.append("Corvina")
peixes.append("Bagre")
peixes.append("Salmão")
peixes.append("Tilápia")

# Removendo valor
peixes.remove("Corvina")

# Listando conteúdo - método 1
for i in range(0, len(peixes)):
    print(peixes[i])
print("")

# Listando conteúdo - método 2
for peixe in peixes:
    print(peixe)
print("")

# Ordenando ascendente
peixes.sort()
for peixe in peixes:
    print(peixe)
print("")

# Ordem descendente
peixes.reverse()
for peixe in peixes:
    print(peixe)
print("")

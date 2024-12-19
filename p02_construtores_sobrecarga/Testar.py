#!python3

import Aluno

aluno1 = Aluno.Aluno()
aluno1.nome = "Fulano da Silva"
if aluno1.ativo:
  print(f"O aluno {aluno1.nome} esta ativo")
else:
  print(f"O aluno {aluno1.nome} não esta ativo")

aluno2 = Aluno.Aluno("Beltrano Gomes")
if aluno2.ativo:
  print(f"O aluno {aluno2.nome} esta ativo")
else:
  print(f"O aluno {aluno2.nome} não esta ativo")
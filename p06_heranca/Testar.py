#!python3

from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

pf = PessoaFisica()
pf.nome = "Fulano da Silva"
pf.cpf = "304.349.920-46"
print(f"{pf.nome}, {pf.cpf}")

pj = PessoaJuridica()
pj.nome = "Empresa XYZ Ltda"
pj.cnpj = "93.064.305/0001-48"
print(f"{pj.nome}, {pj.cnpj}")

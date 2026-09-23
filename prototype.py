from copy import deepcopy


class Funcionario:
    def __init__(self, nome, empresa, setor):
        self.nome = nome
        self.empresa = empresa
        self.setor = setor

    def clone(self):
        return deepcopy(self)

    def dados_funcionario(self):
        return f"{self.nome} - {self.empresa} - {self.setor}"


funcionario1 = Funcionario(
    nome="Kelvyn",
    empresa="Telles Dev",
    setor="TI"
)

funcionario2 = funcionario1.clone()
funcionario2.nome = "Lopes"

print(funcionario1.dados_funcionario())
print(funcionario2.dados_funcionario())
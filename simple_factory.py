from abc import ABC, abstractmethod


class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass


class PagamentoCartaoCredito(Pagamento):
    def pagar(self, valor):
        print(f"Pagamento de R${valor} realizado com cartão de crédito.")


class PagamentoCartaoDebito(Pagamento):
    def pagar(self, valor):
        print(f"Pagamento de R${valor} realizado com cartão de débito.")


class ProcessarPagamentoFactory:

    @staticmethod
    def criar_pagamento(tipo):
        if tipo == "credito":
            return PagamentoCartaoCredito()
        elif tipo == "debito":
            return PagamentoCartaoDebito()
        else:
            raise ValueError("Tipo de pagamento inválido.")


pagamentos = [{"tipo": "credito", "valor": 100}, {"tipo": "debito", "valor": 50}]

for pagamento in pagamentos:
    tipo = pagamento["tipo"]
    valor = pagamento["valor"]
    processador = ProcessarPagamentoFactory.criar_pagamento(tipo)
    processador.pagar(valor)

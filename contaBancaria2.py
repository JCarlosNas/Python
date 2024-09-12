class ContaBancaria:
    def __init__(self, numero_conta, saldo = 0, numero_transacoes = 0):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.numero_transacoes = numero_transacoes

    def depositar (self,valor):
        self.saldo += valor
        self.numero_transacoes += 1

    def sacar (self, valor):
        self.saldo -= valor
        self.numero_transacoes += 1

    def calcular_tarifa (self):
        tarifa_base = CalculadoraTarifas.calcular_tarifa_base()
        tarifa_transacao = CalculadoraTarifas.calcular_tarifa_transacao(self.numero_transacoes)
        tarifa_saldo = CalculadoraTarifas.calcular_tarifa_saldo (self.saldo)
        return tarifa_base + tarifa_transacao + tarifa_saldo

class ContaCorrente(ContaBancaria):
    def __init__(self,numero_conta,saldo = 0, numero_transacoes = 0):
        super().__init__(numero_conta,saldo,numero_transacoes)

class ContaPoupanca(ContaBacaria):
    def __init__(self, numero_conta, saldo = 0, numero_trasacoes = 0 ):
        super().__init__(numero_conta,saldo, numero_trasacoes)

        
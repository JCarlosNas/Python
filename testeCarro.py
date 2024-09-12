class Carro:
      def __init__(self, marca,cor):
          self.marca = marca
          self.cor = cor

      def Ligar(self):
          print ("o carro está ligado")

      def Desligado(self):
          print("o carro está desligado")

      def ExibirInformacoes(self):
          print(self.marca, self.cor)

carro1 = Carro("WV", "azul")
carro2 = Carro("Ford", "vermelho")
carro1.Ligar()
carro2.Desligado()
carro1.ExibirInformacoes()
carro2.ExibirInformacoes()

# class Computador:
#     def __init__(self, marca, memoria_ram, placa_de_video):
#         self.marca = marca
#         self.memoria_ram = memoria_ram
#         self.placa_de_video = placa_de_video
#
#     def Ligar (self):
#             print("estou ligando")
#
#     def Desligar (self):
#         print("estou desligando")
#
#     def ExibirInformacoesDesteComputador(self):
#         print(self.marca, self.memoria_ram, self.placa_de_video)
#
# computador1 = Computador ("Asus","16g", "Nvidia")
# computador1.Ligar()
# computador1.Desligar()


class Moto:
    def __init__(self,marca,cor):
        self.marca = marca
        self.cor = cor

    def Acelerar (self):
        print("a moto esta estou aquecendo")

    def ExibirInformacoes(self):
         print(self.marca, self.cor)

moto1 = Moto ("honda","verde")
moto1.Acelerar()
moto1.ExibirInformacoes()


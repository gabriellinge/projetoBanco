import random

from modulos.Banco import Banco

class Cliente:
   def __init__(self, clienteCPF, clienteNome):
      """
      Iniciar o cadastro do cliente
      :clienteCPF = CPF com 11 números
      :clienteNome = nome completo do cliente
      """
      self.cpf = ''
      self.nomeCompleto = ' '.join(clienteNome.rsplit()).title()
      self.validarCPF(clienteCPF)
      self.cartoes = {}
      self.suportes = {}

   def validarCPF(self, clienteCPF):
      clienteCPF = str(clienteCPF)
      if len(str(clienteCPF)) == 11:
         cpf = [
                [i for i in clienteCPF[0:3] ], "-",
                [i for i in clienteCPF[3:6] ], "-",
                [i for i in clienteCPF[6:9] ], "-",
                [i for i in clienteCPF[9:12]]
               ]
         for i in cpf:
            self.cpf += ''.join(i)


# DEBUG

if __name__ == "__main__":
   nomes = ['Gabriel', 'Ricardo', 'Lucas', 'Daniel', 'Guilherme', 'Matheus']
   sobrenomes = ['Silva', 'Oliveira', 'Santos', 'Glória', 'Smith']
   c1 = Cliente(random.randint(10000000000, 90000000000), f"{random.choice(nomes)} {random.choice(sobrenomes)}")
   c2 = Cliente(random.randint(10000000000, 90000000000), f"{random.choice(nomes)} {random.choice(sobrenomes)}")
   banco = Banco('BuBank')

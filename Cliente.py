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

   def validarCPF(self, clienteCPF):
      if len(str(clienteCPF)) == 11:
         cpf = [
                [i for i in clienteCPF[0:3] ], "-",
                [i for i in clienteCPF[3:6] ], "-",
                [i for i in clienteCPF[6:9] ], "-",
                [i for i in clienteCPF[9:12]]
               ]
         for i in cpf:
            self.cpf += ''.join(i)

from modulos.Banco import Banco

class Cliente:
   def __init__(self, clienteCPF, clienteNome):
      """
      Iniciar o cadastro do cliente
      :clienteCPF = CPF com 9 caracteres
      :clienteNome = nome completo do cliente
      """
      
      self.clienteCPF = clienteCPF
      self.clienteNome = clienteNome

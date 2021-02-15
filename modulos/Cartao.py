import random

class Cartao:
   def __init__(self, banco, numeracao=None):
      self.banco = banco
      self.transferenciasComuns = {}
      
      self.numeracao = random.randint(1000000000, 9000000000) if not numeracao else numeracao

      self.debito = False
      self.credito = False

      self.saldo = 0
      self.limite = 0

   def totalClientes(self):
      return len(self.clientes)

   def fazerTransferencia(self, valor=0, cpf='', nomeCompleto=''):
      pass

   def fazerPagamento(self):
      pass

   def fazerSaque(self, valor):
      pass

   def depositar(self, valor):
      saldo = self.banco.confirmarDeposito(valor)
      self.saldo += saldo

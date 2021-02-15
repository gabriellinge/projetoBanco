from modulos.Cartao import Cartao

class Banco:
   def __init__(self, bancoNome):
      """
      Iniciar a criação do banco
      :bancoNome = Nome do banco
      """
      self.clientes = {}
      
      self.nome = bancoNome
      self.capital = 0
      self.caixa = 0
      self.juros = 0

   def adicionarCliente(self, cliente):
      cliente.cartao = Cartao(self)
      self.clientes[cliente.clienteCPF] = cliente
   
   def totalClientes(self):
      return len(self.clientes)

   def autorizarTransferencia(self):
      pass

   def autorizarPagamento(self):
      pass

   def autorizarSaque(self):
      pass

   def confirmarDeposito(self, valor=0):
      self.bancoCaixa += valor
      return valor

from modulos.Cartao import Cartao

class Banco:
   def __init__(self, bancoNome):
      """
      Iniciar a criação do banco
      :bancoNome = Nome do banco
      """
      self.cartosValidos = {}
      self.clientes = {}
      
      self.nome = bancoNome
      self.capital = 0
      self.caixa = 0
      self.juros = 0

   def adicionarCliente(self, cliente):
      if self.nome in cliente.cartoes:
         self.cartoes[self.nome].append(Cartao(self, cliente.nome))
      else:
         self.cartoes[self.nome] = [Cartao(self, cliente.nome)]
      self.cartosValidos[cliente.cartao.numeracao] = cliente.cartao
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

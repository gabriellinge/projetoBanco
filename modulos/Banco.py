from modulos.Cartao import Cartao
from modulos.Suporte import Suporte

class Banco:
   def __init__(self, bancoNome):
      """
      Iniciar a criação do banco
      :bancoNome = Nome do banco
      """
      self.cartoes = {}
      self.clientes = {}
      
      self.nome = bancoNome
      self.capital = 0
      self.caixa = 0
      self.juros = 0

   def adicionarCliente(self, cliente):
      """
      Adicionar um cliente ao banco
      :cliente - Obj Cliente
      """
      if not cliente.cpf in self.clientes:
         self.clientes[cliente.cpf] = cliente
         cliente.suportes[self.nome] = Suporte(self, cliente)
         # self.gerarCartao(cliente)
      
   def gerarCartao(self, cliente, senha="0000", tipo="fisico"):
      cartao = Cartao(self, cliente)
      if self.nome in cliente.cartoes and not tipo in self.cartoes[self.nome]:
         self.cartoes[self.nome].append({tipo: cartao})
         cliente.cartoes[self.nome].append({tipo: cartao})
      else:
         self.cartoes[self.nome] = [{tipo: cartao}]
         cliente.cartoes[self.nome] = [{tipo: cartao}]

   def cancelarCartao(self):
      pass

   def removerCliente(self, cliente):
      if self.nome in cliente.cartoes:
         del self.cartoes[self.nome]
   
   def totalClientes(self):
      """
      Retorna o total de clientes no banco
      """
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

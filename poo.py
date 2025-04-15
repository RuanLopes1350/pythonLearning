# Classes
# class Pessoa:
#     def __init__(self, nome, idade) -> None:
#          self.nome = nome
#          self.idade = idade
#     def saudacao(self):
#         return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."
    

# Objetos
# pessoa1 = Pessoa("Ruan", 24)
# mensagem1 = pessoa1.saudacao()
# print(mensagem1)

# pessoa2 = Pessoa("Luis",19)
# mensagem2 = pessoa2.saudacao()
# print(mensagem2)

# Herança e Polimorfismo
# class Animal:
#     def __init__(self, nome) -> None:
#         self.nome = nome

#     def andar(self):
#         print(f"O animal {self.nome} andou.")
    
#     def emitir_som(self):
#         pass

# class Cachorro(Animal):
#     def emitir_som(self):
#         return "Latidos"
    
# Encapsulamento
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__sald -= valor

    def consultar_saldo (self):
        return self.__saldo
    
cont = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancária: {cont.consultar_saldo()}")
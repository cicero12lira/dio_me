import os


class Banco:
    def __init__(self, saldo_inicial=0, limite_saque=1000):
        self.saldo = saldo_inicial
        self.limite_saque = limite_saque
        self.valor_sacado = []

    def depositar(self):
        valor = float(input('Valor do deposito: '))
        os.system('cls')
        if valor <= 0:
            print("\nDepósito falhou: valor deve ser positivo.")
        else:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} \nREALIZADO COM SUCESSO!")

    def sacar(self):
        valor = float(input('Valor do saque: '))
        os.system('cls')
        self.valor_sacado.append(valor)
        sacado = sum(self.valor_sacado)
  
        
        if valor <= 0:
            print("Saque falhou: valor deve ser positivo.")
        elif sacado > self.limite_saque:
            print(f"Saque falhou: valor excede o limite de saque de R${self.limite_saque:.2f}.")
            self.valor_sacado.pop()
            if self.valor_sacado != []:
                print(f'Sacado hoje: R$ {self.valor_sacado}')
        elif valor > self.saldo:
            print(f"Saque falhou: saldo insuficiente. Saldo atual: R${self.saldo:.2f}.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} \nREALIZADO COM SUCESSO!\n")
            saque_hoje = sum(self.valor_sacado)
            print(f'Saque hoje R$ {saque_hoje}, limite neste terminal: R$ {self.limite_saque}')
            limite_restante = self.limite_saque - saque_hoje
            print(f'\nVocê ainda pode sacar neste terminal R$ {limite_restante}')

    def consultar_saldo(self):
        print(f"\nSaldo atual: R$ {self.saldo:.2f}\n")
        banco.continuar()

    def sair(self):
        print("Até breve!")
        quit()
    
    def continuar(self):
        continuar = input('Continuar? [s/n]: ')
        if continuar == 's':
            pass
        elif continuar == 'n':
            banco.sair()
        else:
            print('Escolha uma opção valida:')
            banco.continuar()


# Exemplo de uso:
banco = Banco(saldo_inicial=0, limite_saque=1000)

menu = """

########### Menu #############

        [d]epositar
        [s]acar
        [e]xtrato
        [ss]air

###############################

-> """

while True:
    os.system('cls')
    opcao = input(menu)
    if opcao == "d":
        os.system('cls')
        banco.depositar()
        banco.consultar_saldo()

    elif opcao == "s":
        os.system('cls')
        banco.sacar()
        banco.consultar_saldo()

    elif opcao == "e":
        os.system('cls')
        banco.consultar_saldo()
        banco.continuar()

    elif opcao == "ss":
        os.system('cls')
        banco.sair()

    else:
        os.system('cls')
        print('Escolha uma das opções:')


banco.consultar_saldo()
banco.depositar(300)
banco.sacar(200)
banco.sacar(2000)  # Tentativa de saque acima do limite
banco.sacar(700)   # Tentativa de saque com saldo insuficiente

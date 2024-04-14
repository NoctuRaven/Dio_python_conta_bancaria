class Conta_Bancaria():
    
    def __init__(self,cpf,nome,valor):
        self.cpf = cpf
        self.nome = nome
        self.valor = valor
        self.extrato = []
        
        
    def add_value(self,valor):
        try:
            valor = float(valor)
            if valor>0:
                self.valor += valor
                self.extrato.append("{:.2f}".format(valor))
                print(f"R${valor} adicionado a conta")
                print(f"Saldo atual: R${"{:.2f}".format(self.valor)}")
            else:
                raise
        except:
            print("Impossivel concluir a transação: Digite um valor válido")
            
    def show_extract(self):
        print("Ultimas transações:")
        if not self.extrato:
            print("**EMPTY**")
        else:
            for val in self.extrato:
                print(f"R${"{:.2f}".format(float(val))}")
    
    def check_withdraw(self):
        ac = 0
        if not self.extrato:
            return 0
        for v in self.extrato:
            if float(v) < 0:
                ac+=1
        return ac
        
    
    def withdraw_value(self,valor):
        try:
            valor = float(valor)
            if valor<0:
                raise
            if self.check_withdraw()<3:
         
                if valor > 500:
                    print(f"O valor informado esta a cima do limite de $500")
                else:
                    if (self.valor < valor ):
                        print(f"O valor informado esta a cima do saldo atual de ${self.valor}")
                    else:
                        self.valor -= float(valor)
                        print(f"R${valor} retirado da conta")
                        print(f"Saldo atual R${"{:.2f}".format(self.valor)}")
                        self.extrato.append("{:.2f}".format(-1*valor))
            else:
                print("Numero de saques excedido")
        except:
            print("Impossivel concluir a transação: Digite um valor válido")
                
            

nova_conta = Conta_Bancaria(nome="Pessoa",cpf="123456789",valor=0.00)

class Caixa_Eletronico:
    def __init__(self):
        pass
    def interface():
        print(f"Bem vindo {nova_conta.nome}")
        stay_in_loop = True
        while stay_in_loop:
            opcao = input(f"""Escolha uma das opções: 
                        a) Saque
                        b) Deposito
                        c) Extrato
                        d) sair
                        
                        """)
            if opcao=="a":
                saque = input("Digite o valor que deseja sacar")
                nova_conta.withdraw_value(saque)
                res = input("Deseja fazer outra operação? s/n ")
                stay_in_loop = res=="s"
            elif opcao=="b":
                deposito = input("Digite o valor do deposito")
                nova_conta.add_value(deposito)
                res = input("Deseja fazer outra operação? s/n ")
                stay_in_loop = res=="s"
            elif opcao=="c":
                nova_conta.show_extract()
                res = input("Deseja fazer outra operação? s/n ")
                stay_in_loop = res=="s"
            else:
                stay_in_loop = False

caixa_1 = Caixa_Eletronico

caixa_1.interface()
        
        
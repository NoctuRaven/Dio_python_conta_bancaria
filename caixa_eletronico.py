class Conta_Bancaria():
    
    def __init__(self,cpf,nome,valor):
        self.cpf = cpf
        self.nome = nome
        self.valor = valor
        self.extrato = []
        
        
    def add_value(self,valor):
        try:
            if float(valor)>0:
                self.valor += valor
                self.extrato.append(valor)
                print(f"${valor} adicionado a conta")
                print(f"Saldo atual: ${self.valor}")
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
                print(f"${val}")
    
    def check_withdraw(self):
        ac = 0
        if not self.extrato:
            return 0
        for v in self.extrato:
            if v < 0:
                ac+=1
        return ac
        
    
    def withdraw_value(self,valor):
        try:
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
                        print(f"${valor} retirado da conta")
                        print(f"Saldo atual ${self.valor}")
                        self.extrato.append(-1*(valor))
            else:
                print("Numero de saques excedido")
        except:
            print("Impossivel concluir a transação: Digite um valor válido")
                
            

nova_conta = Conta_Bancaria(nome="Pessoa",cpf="123456789",valor=0.00)

nova_conta.add_value(30)
nova_conta.add_value(-30)
nova_conta.withdraw_value(10)
nova_conta.add_value(700)
nova_conta.withdraw_value(600)
nova_conta.add_value("aaa")
nova_conta.withdraw_value(10000)
nova_conta.withdraw_value(-10000)
nova_conta.withdraw_value(10)
nova_conta.withdraw_value(10)
nova_conta.withdraw_value(10)
nova_conta.show_extract()
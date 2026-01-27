valor_conta=1000

while True:
    opcao=int(input("escolha uma opção:\n (1) depositar\n (2) sacar\n (0) sair\n= "))
    if opcao==0:
        break

    elif opcao==1:
        depositar=int(input("Digite o valor do deposito: "))
        valor_conta+=depositar
        print(f"Valor da conta: {valor_conta}")
    elif opcao==2:
        saque=int(input("Digite o valor do saque: "))
        
        if saque>valor_conta:
            print(f"saldo indisponivel")  
            print(f"saldo R${valor_conta}")  
            
        else:
            valor_conta-=saque
            print(f"Valor da conta disponivel R${valor_conta}")
            print(f"Valor do saque R${saque}")
            
           
             

    else:
        print("valor invalido,tente novamente!")
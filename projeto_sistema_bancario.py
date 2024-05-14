menu = '''

============= Porquinho Bank =============
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

==========================================
    Obrigado por oncc, usar nosso 
           oncc! ba-banco.
'''

saldo = 0.0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":

        valor = float(input(("Informe o valor a ser depositado: ")))

        if valor > 0:

            saldo += valor
            extrato += f"Depósito: R$ +{valor:.2f}\n"
            print(f"Valor de R$ {valor:.2f} depositado com sucesso! oncc..")  
            print(f"Saldo atual: R$ {saldo:.2f}")
            #print("Valor depositado com sucesso. oncc..")
            #extrato += str(valor) + "\n"

        else: 
            print("Não foi possível completar a operação, valor deve ser positivo. oncc..")
    
    elif opcao == "2":

        saque = float(input(("Informe o valor do saque: ")))

        if saque > 0: 
            if saque <= limite:
                if saque < saldo:
                    if numero_saques <= LIMITE_SAQUES:
                        saldo -= saque
                        numero_saques +=1
                        extrato += f"Saque: R$ -{saque:.2f}\n" 
                        print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
                        print(f"Saldo atual: R$ {saldo:.2f}")
                        #print("Saque realizado com sucesso!")
                    else:
                        print("Limite de saques atingidos, não foi possível sacar.")
                else:
                    print("Saldo insuficiente para esta transação")  
            else: 
                print(f"Não foi possivel sacar, o limite de saque por vez é de: R$ {limite}")
        else: 
            print("O saque deve ser positivo.")
  
    elif opcao == "3": 
        print(f"""
            ************** EXTRATO BANCÁRIO **************   

{extrato}
 
            **********************************************
            """)

    elif opcao == "0":
        print("O porquinho bank agradece sua prefêrencia, tenha um ótimo dia! oncc..")

        break

    else:
         print("Opção invalida, tente novamente ou entre em contato com o gerente. oncc..")
opcao = 0
saque = 0
deposito = 0
limite = 500
saldo = 0
limite_saque = 0

menu = """ 
------MENU------

[1] Extrato
[2] Depósito
[3] Saque
[4] Sair 

----------------
"""

extrato = """
------EXTRATO------
"""

while True:
    print(menu)
    opcao = int(input("Digite a opção escolhida... "))

    if (opcao == 4):
        print("\nObrigado por utilizar o RND Bank, satisfação em tê-lo como cliente!\n")
        break

    elif (opcao == 3):
        if (limite_saque == 3):
            print("\nVocê excedeu o número de saques! Volte em 24h.")
        else:
            saque = int(input("\nDigite o valor que deseja sacar... \n(Mín: R$ 10,00\nMax R$ 500,00)\nR$ "))

            while (saque < 10 or saque > 500 or saque > saldo):
                saque = int(input("\nValor inválido!\nDigite o valor que deseja sacar... \n(Mín: R$ 10,00\nMax R$ 500,00)\nR$ "))

            limite_saque +=1
            saldo -= saque      
            extrato += (f"\n\nSaque........R$ {saque:.2f}") 
            print("\nSaque realizado com sucesso!")   

    elif (opcao == 2):
        deposito = int(input("\nDigite o valor à ser depositado...\n(Mín: R$ 10,00)\nR$ "))

        while (deposito < 10):
            deposito = int(input("\nValor inválido!\nDigite o valor à ser depositado...\n(Mín: R$ 10,00)\nR$ "))
    
        saldo += deposito
        extrato += (f"\n\nDepósito........R$ {deposito:.2f}")
        print("\nDepósito realizado com sucesso!")
    
    elif (opcao == 1):
        print (extrato, (f"\n\n\nSALDO ATUAL: R$ {saldo:.2f}"))

    else:
        print("Opção inválida!")


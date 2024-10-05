from datetime import datetime
import pytz

opcao = 0
saque = 0
deposito = 0
limite = 500
saldo = 0
limite_saque = 0

menu = """ 
----------------MENU----------------

[1] Extrato
[2] Saque
[3] Depósito
[4] Sair 

------------------------------------
"""

extrato = """
---------------EXTRATO---------------
"""

def registro_trans_data_hora():

    data_utc = datetime.now(pytz.utc)
    sao_paulo = pytz.timezone('America/Sao_Paulo')
    data_sp = data_utc.astimezone(sao_paulo)
    data_formatada = data_sp.strftime("%d/%m/%Y %H:%M:%S")
    return data_formatada

def operacao_saque():

    global limite_saque, saque, saldo, extrato

    if limite_saque == 3:
        print("\nVocê excedeu o número de saques! Volte em 24h.")
    
    else:
        saque = int(input("\nDigite o valor que deseja sacar... \nMín: R$ 10,00\nMax R$ 500,00\nR$ "))

        while saque < 10 or saque > 500:
            saque = int(input("\nValor inválido!\nDigite o valor que deseja sacar... \n(Mín: R$ 10,00\nMax R$ 500,00)\nR$ "))

        if saque > saldo:
            print("Seu saldo é insuficiente! Digite outro valor ou deposite em sua conta.")
        
        else:
            limite_saque +=1
            saldo -= saque      
            extrato += (f"\n\nSaque - R$ {saque:.2f}          {registro_trans_data_hora()}") 
            print("\nSaque realizado com sucesso!")

def operacao_deposito():

    global deposito, saldo, extrato

    deposito = int(input("\nDigite o valor à ser depositado...\n(Mín: R$ 10,00)\nR$ "))

    while (deposito < 10):
        deposito = int(input("\nValor inválido!\nDigite o valor à ser depositado...\n(Mín: R$ 10,00)\nR$ "))

    saldo += deposito
    extrato += (f"\n\nDepósito - R$ {deposito:.2f}          {registro_trans_data_hora()}")
    print("\nDepósito realizado com sucesso!")

def menu_interno():

    global menu, opcao, extrato, saldo

    while True:
        
        print(menu)
        opcao = int(input("Digite a opção escolhida... "))

        if (opcao == 1):
            print (extrato, (f"\n\n\nSALDO ATUAL: R$ {saldo:.2f}          Atualizada em: {registro_trans_data_hora()}"))

        elif (opcao == 2):
            operacao_saque()

        elif (opcao == 3):
            operacao_deposito()
        
        elif (opcao == 4):
            print("\nObrigado por utilizar o RND Bank, satisfação em tê-lo como cliente!\n")
            break

        else:
            print("Opção inválida!")

while True:
    if (opcao == 4):
        break
    else:
        (menu_interno())
def calculo(nm1,nm2, sin):
    if sin == 1:
        resp = nm1 + nm2
    elif sin == 2:
        resp = nm1 - nm2
    elif sin == 3:
        resp = nm1 / nm2
    elif sin == 4:
        resp = nm1 * nm2
    else:
        print("Opção invalida, por favor digite operação valída.")
    return(int(resp))



while sair == False:
    print("Digite o 1 númeroque deseja usar, em seguida o segundo número e logo após uma operação das seguintes:")

    print("1 - Soma, 2 - Subtração, 3 - Divisão, 4 - Multiplicação.")
    num1 = int(input("Digite o número 1: "))
    num2 = int(input("Digite o número 2: "))
    op = int(input("Digite o operador matematico: "))
    resp = calculo(num1, num2, op)
    print(f"O resultado da sua conta foi: {resp}")
    print("Para fazer outra operação digite 1, para encerrar digite 2.")
    wt = int(input())
    if wt == 1:
        sair = False
    elif wt == 2:    
        sair = True
        

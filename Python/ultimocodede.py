
act = True

while act == True:

    lista_de_afazeres = ["limpar o quarto", "arrumar a cama" , "escovar os dentes", "se arrumar para o trabalho", "salvar o mundo de uma destruição em massa"]

    try:
        print(f"\nOlá, sua lista de afazeres se encontra assim atualmente:")
        ota = 0
        sndi = len(lista_de_afazeres)
        for i in range(sndi):
            print(f"{ota} {lista_de_afazeres[i]}")
            ota = ota + 1

        print("\nDigite uma das opções de ações a seguir:")
        print(" 1 - Para adicionar uma nova tarefa \n 2 - Para verificar sua lista de tarefas \n 3 - Para apagar algum item da sua lista \n 4 - Sair \n")

        ato = int(input("Digite uma das opções anteriores: "))

        if ato <= 0:
            print("Opção invalida")
            act = False
            sact = int(input("Digite 4 para sair ou 5 para recomeçar: "))
            if sact == 4:
                act = False
            elif sact == 5:
                act = True
            else:
                print("Error!! Reiniciando...")
                act = True
        if ato == 1:
            ato1 = True
            while ato1 == True:
                add = str(input("O que deseja adicionar á sua lista de afazeres? "))
                lista_de_afazeres.append(add)
                nota = 0
                indi = len(lista_de_afazeres)

                for i in range(indi):
                    print(f"{nota} - {lista_de_afazeres[i]}")
                    nota = nota + 1
            
                tact = int(input("Digite 1 para repetir a ação atual, 4 para sair ou 5 para recomeçar "))

                if tact == 1:
                    ato1 = True
                elif tact == 4:
                    act = False
                elif tact == 5:
                    ato1 = False
                    act = True
                else:
                    print("ERRO!! Finalizando code...")     
                    break  
            
        elif ato == 2:
            print("A sua lista de afazeres se encontra assim atualmente: ")
            ota = 0
            sndi = len(lista_de_afazeres)
            for i in range(sndi):
                print(f"{ota} {lista_de_afazeres[i]}")
                ota = ota + 1

            sact = int(input("Digite 4 para sair ou 5 para recomeçar: "))
            if sact == 4:
                act = False
            elif sact == 5:
                act = True
            else:
                print("Error!! Reiniciando...")
                act = True
        elif ato == 3:
            ato3 = True
            while ato3 == True:
                notas = 0
                indic = len(lista_de_afazeres)
                for i in range(indic):
                    print(f"{notas} - {lista_de_afazeres[i]}")
                    notas = notas + 1

                add3 = int(input("Qual o indice do item q deseja remover da sua lista de afazeres? "))
                lista_de_afazeres.pop(add3)
                notas = 0
                indic = len(lista_de_afazeres)
                
                print("Lista de afazeres atualizada!! Atualmente esta assim:")

                for i in range(indic):
                    print(f"{notas} - {lista_de_afazeres[i]}")
                    notas = notas + 1
            
                qact = int(input("Digite 1 para repetir a ação atual, 4 para sair ou 5 para recomeçar "))

                if qact == 1:
                    ato3 = True
                elif qact == 4:
                    act = False
                elif qact == 5:
                    ato3 = False
                    act = True
                else:
                    print("ERRO!! Finalizando code...")     
                    break  
        elif ato == 4:
            act = False
            break
        else:
            print("Use somente um número de opção valido.")
            act = True

    except ValueError:
        print("ERRO!! Use números e letras somente onde forem chamados!")

    except:
        print("ERRO!!")
        break

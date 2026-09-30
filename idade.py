altura= float(input("Qual a sua altura?: "))
idade = int(input("Qual a sua idade?: "))
if altura>=1.40 and idade>=12:
    print("Acesso permitido! Bom passeio.")
else:
    if altura>=1.40 and idade<12:
        print("Acesso negado. Você não tem a idade minima")
    elif altura<1.40 and idade>=12:
        print("Acesso negado. Você não tem a altura mínima")
    else:
        print(" Acesso negado, Você não possui nenhum dos dois")
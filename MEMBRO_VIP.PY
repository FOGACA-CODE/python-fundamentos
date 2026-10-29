idade = int(input("Digite sua idade: "))
membro_vip = input("Você é membro VIP? (s/n): ").lower() == 's'
if idade != 18 and  idade>=12 and idade<=25 or membro_vip:
    print("Você tem acesso ao brinde exclusivo!")
elif idade == 18 or not membro_vip:
    print("Você não tem acesso ao brinde exclusivo.")
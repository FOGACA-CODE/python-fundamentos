nota = float( input("qual a sua nota? ") )
renda = float( input("qual a sua renda? ") )
codigo_especial = input("você possui algum código especial? (sim/não) ").lower() == 'sim'
advertencia = input("você possui alguma advertência? (sim/não) ").lower() == 'sim'
if nota >=8.0 and renda <=3000 and advertencia == False:
    print("Você está aprovado!")
elif nota>8.0 or renda>3000 or advertencia == True:
    print("Você não está aprovado!")
primeiro_valor = int(input("Digite um valor: "))
segundo_valor = int(input("Digite outro valor: "))
if primeiro_valor > segundo_valor:
    print(f"O maior valor é: {primeiro_valor}")
elif segundo_valor > primeiro_valor:
    print(f"O maior valor é: {segundo_valor}")
else:
    print("Os valores são iguais.")
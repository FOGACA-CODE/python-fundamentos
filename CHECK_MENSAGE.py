mensagem = "Hoje o dia está ótimo e muito bonito!"
palavras_proibidas = ["spam", "fake", "ofensa", "golpe"]
if mensagem_segura = not any(palavra in mensagem for palavra in palavras_proibidas):
    print("Mensagem segura")
    else:
    print("Mensagem contém palavras proibidas")
cargo = "admin"
conta_bloqueada = False
if cargo == "admin" and not conta_bloqueada:
    print("Acesso permitido")
    elif cargo == "admin" and conta_bloqueada:
    print("Acesso negado")
    else: cargo == "gerente" and not conta_bloqueada:
    print("Acesso permitido")
    elif cargo == "gerente" and conta_bloqueada:
    print("Acesso negado")
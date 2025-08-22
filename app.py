email = input("Digite seu email: ")
emailBanco = "analia.nai"
if (email == emailBanco):
    senha = input("Digite sua senha: ")
    senhaBanco = "123@"
    if (senha == senhaBanco):
        print("Bem-vinda, Analia!")
    else:
        print("Senha incorreta. Tente novamente.")
elif (email != emailBanco):
    print("Não foi possível encontrar sua Conta do Google.")
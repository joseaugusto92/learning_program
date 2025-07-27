# Credenciais corretas
usuario_correto = "admin"
senha_correta = "1234"

# Número de tentativas permitidas
tentativas = 3

for tentativa in range(tentativas):
    # Solicita usuário e senha
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    # Verifica se estão corretos
    if usuario == usuario_correto and senha == senha_correta:
        print(f"\nBem-vindo, {usuario}!")
        break
    else:
        restantes = tentativas - tentativa - 1
        if restantes > 0:
            print(f"\nCredenciais incorretas. Você ainda tem {restantes} tentativa(s).\n")
        else:
            print("\nNúmero máximo de tentativas atingido.\n")
            for _ in range(3):
                print("Acesso bloqueado.")



  else:
        chances -= 1
        if chances > 0:
            for i in range (3):
                print(f"Credenciais erradas! Você só tem mais {chances} tentativas")
                if i == 3:
                    print("Acesso bloqueado."z
            
                
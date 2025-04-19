senha = 1478
usuario = "chefe"
chances = 3

for i in range (1,4):
    login = str(input("Digite o seu usuário: "))
    senha2 = int(input("Digite a senha: "))
    if login == usuario and senha2 == senha:
        print("Acesso LIBERADO BEM VINDO CHEFE!! ")
        break
    else:
        chances -= 1
        print(f"Credenciais erradas! Você só tem mais {chances} tentativas")
        if chances == 0:
            print("Limite de tentativas Excedidas, ACESSO BLOQUEADO")
            break
        
        
     
                
            
    
    


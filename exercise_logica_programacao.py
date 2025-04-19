# idade = int(input("DIGITE A SUA IDADE: "))


# temhabilitacao = int(input(" VOCÊ POSSUI HABILITAÇÃO? 1 SIM OU 2 NÃO:  "))



# if idade >= 18 and temhabilitacao == 1:
#     print("PARABÉNS, VOCÊ PODE DIRIGIR!!")   
# elif idade >= 18 and temhabilitacao == 2: 
#     print("VOCÊ NÃO PODE DIRIGIR,TIRE A SUA HABILITAÇÃO !!! ") 
# elif idade < 18 and temhabilitacao == 1:
#     print ("MENTIRA, MENOR DE IDADE NÃO TEM HABILITAÇÃO, TU NÃO PODE DIRIGIR!!!")
# elif idade < 18 and temhabilitacao == 2:
#     print("VOCÊ NÃO PODE DIRIGIR, SAI DAQUI !!!")

#   ________________________________________________________
  
# nota1 = float(input("Insira a nota do semestre 1: "))
# nota2 = float(input("Insira nota do semestre 2: "))

# soma = nota1 + nota2

# print("Se a sua média for menor que 6, você será reprovado")

# media = soma / 2
    
# print(media)

# __________________________________________________________


# nota1 = float(input("Insira a nota do semestre 1: "))
# nota2 = float(input("Insira nota do semestre 2: "))

# soma = nota1 + nota2

# media = soma / 2

# if media >= 6:
#     print("SUA NOTA É: ", media , "APROVADO!" )
# else:
#     print("As notas são menores 6, REPROVADO!", media)

# ______________________________________________________________

# precoproduto = float(input("Insira o preço do produto para saber o Desconto: "))

# desconto = (precoproduto * 5) / 100

# valorfinal = precoproduto - desconto

# print("DESCONTO DO SEU PRODUTO É: ", desconto , "Valor final é: ", valorfinal)

# ____________________________________________________________________


# num = int(input("INSIRA UM NUMERO: "))

# num *= 2

# print("O NUMERO foi dobrado, esse é o resultado: ", num)

# _____________________________________________________________________


# frase = str(input(" Escreva uma Frase: "))

# letray = "y"
# letraw = "w"
# letrab = "b"

# resultado1 = "y"  and "w" and "b" in frase

# print(resultado1)


#________________________________________________________________________

# frase = str(input(" Escreva uma Frase: "))

# word = "Brasil"


# resultado = word in frase

# print(resultado)

# _________________________________________________________________________

# frase = str(input("Escreva uma FRASE qualquer: "))

# word1 = 'b'

# if word1 in frase:
#     print("Na sua frase tem a letra B")
# else:
#     print("Sua frase não tem Letra B")


# num = 21

# if num > 20:
#     print("o numero é maior que 20")
# elif num > 10:
#     print("O numero é maior que 10")

# __________________________________________________________


# num = int(input(" Digite um numero : "))



# if num % 2 >=1:
#     print(" o NUMERO que você digitou é ímpar ")
# else:
#     print(" o NUMERO é par !")

# _____________________________________________________________

# FAZER ATIVIDADE 12 DA AULA 02


# peso = int(input("Vamos agora calcular o seu IMC, DIGITE o seu PESO: "))
# altura = float(input("Agora DIGITE a ALTURA: "))

# imc = peso / (altura ** 2)

# if imc >= 18.6 and imc <= 24.9:
#     print("Seu peso está NORMAL !!! ",imc)
# elif imc >= 25.0 and imc <= 29.9:
#     print('Você está com SOBREPESO, Atenção !!!', imc)
# elif imc >= 30.0 and imc <= 34.9:
#     print('Você está com ACIMA DO PESO, URGENTE PERDE PESO !!!', imc)
# elif imc <= 18.5:
#     print('Você está abaixo do PESO!!!', imc)
    
# _______________________________________________________________


# nome = str(input("Digite o seu USUARIO: "))
# senha = int(input("Digite a SENHA: "))

# if nome == 'admin' and senha == 1234:
#     print("Acesso PERMITIDO, Bem Vindo!")
# elif nome == 'admin' and senha != 1234:
#     print("USUARIO correto mas senha ERRADA")
# else:
#     print ("USUARIO OU SENHA INCORRETOS !!!")

#____________________________________________________________

# valor = float(input(" Qual valor total dos produtos comprados? "))
# qtd = int(input(" Qual a quantidade de itens comprados? "))

# if qtd >= 10:
#     valor = valor - (valor*0.1)
#     print("parabens você ganhou um desconto!", valor)

# else:
#     print("como você pegou menos de 10 itens não tem desconto", valor)

#_____________________________________________________________

# AULA 3 WHILE

# soma = 0
# numero = 1

# while numero <=20:
#     soma += numero
#     numero += 1
# print(soma)


# num1 = 1


# while num1 <= 10:
#     print(num1)
#     num1 += 1
# print("acabou")


# _____________________________________________

# EXERCICIO 2

# num1 = 0
# num2 = 1

# while num2 <= 9:
#     num1 += num2
#     num2 += 1
#     print(f"{num2} + {num1}  =", num1)


#_________________________________________________

# x = 0

# if x > 0:
#     print("Positivo")
# elif x <0:
#     print("Negativo")
# else:
#     print("Zero")

# ___________________________________________
# Atividade 1
# x = 0

# while x <=10:
#     print(x)
#     x += 1

# _____________________________________

# Atividade 2 Soma de Números de 1 a 100:
# Escreva um programa que use um laço while para
# somar os números de 1 a 100 e exiba o resultado.

# x = 0
# y = 1 

# while y <= 100:
#     x += y
#     print(x)
#     y+=1
# print(x)
   
# __________________________________________

# Atividade 03:
# Tabuada de um Número:
# Faça um programa que solicite um número ao usuário e use
# um laço while para exibir a tabuada desse número (de 1 a 10).

# num = int(input('Digite um numero para ver a tabuada dele: '))

# mult = 1

# while mult <10:
#     print(f'{num} x {mult} = {num * mult}')
#     mult +=1
    
# ________________________________________________

# Atividade 04:
# Contagem Regressiva:
# Desenvolva um programa que use um laço while para exibir
# uma contagem regressiva de 10 até 1 e, em seguida, exiba
# "Feliz Ano Novo!".

# x = 10


# while x <= 10 and x >0:
#     print(x)
#     x -= 1
# print ("Feliz Ano NOVO!!!")    

# versão professor:


# count = 10

# while count > 0:
#     print(count)
#     count -= 1
# print('Feliz Ano novo!!!!!!')    

#____________________________________________________


# Atividade 05:
# Contagem até o Número Inserido:
# Crie um programa que solicite um número ao usuário e use
# um laço while para contar de 1 até o número inserido,
# exibindo apenas os números ímpares.

# num = int(
# input("Digite um numero para saber os numeros ímpares até ele: ")
# )
# x = 1 

# while  x <= num:
#     if x % 2 != 0:
#         print(x)
#     x +=1
    
#________________________________________________________

# Atividade 06:
# Soma de Números Positivos:
# Escreva um programa que solicite números ao usuário até
# que ele digite um número negativo, somando apenas os
# números positivos inseridos.

# num = int (input("Insira um numero, vamos mostrar os ímpares até ele: "))

# x = 1

# while x <= num:
#     if x % 2 != 0:
#      print (x)
#     x += 1
    
    

# num = int (input("Insira um numero, vamos mostrar os pares até ele: "))

# x = 1  

# while x <= num:
#     if x % 2 == 0:
#         print (x)
#     x += 1

# ____________________________________________________________________________

# Atividade 07:
# Tabuada com Condicional:
# Faça um programa que solicite um número ao usuário e use
# um laço while para exibir a tabuada desse número (de 1 a 10),
# mas apenas para os resultados que forem múltiplos de 3.

# num = int(input(" Digite um numero para Tabuada com resultados multiplos de 3: "))

# mult = 1

# while mult <= num:
#     result = num * mult
#     if result % 3 == 0:
#         print(f' {num} x {mult} =', result)
#     mult += 1
    
# _____________________________________________________________________________


# Atividade 08:
# Média de Notas:
# Desenvolva um programa que solicite as notas dos alunos até
# que o usuário digite -1. Calcule e exiba a média das notas
# inseridas.
# ______________________________________________

# Atividade 09:
# Contagem até 10:
# Crie um programa que use um laço while para contar de 1 a 10
# e termine quando atingir 10.

# x = 1

# while x <=10:
#     print(x)
#     x += 1

#______________________________________________

# Atividade 10:
# Escreva um programa que use um laço while para somar
# números consecutivos começando de 1 e termine quando
# a soma atingir ou ultrapassar 50.

# x = 1
# y = 1


# while x > 0:
#     x += y
#     print(x)
#     if x > 50:
#         break

#___________________________________________________

# Atividade 11:
# Entrada Válida:
# Crie um programa que solicite ao usuário um número entre 1 e 10.
# Continue pedindo até que o usuário forneça um valor válido.


# x = 9

# while x < 10:
#     num = int (input(" Digite um numero 1 a 10 para saber se é o correto: "))
#     if num == x:
#         print("PARABÉNS VOCÊ ACERTOU !!!")
#         break
#     if num != x:
#         print ("Errou ! Tente de novo,")
# ________________________________________________________

#12
# Desenvolva um programa que peça ao usuário para digitar uma
# senha e continue pedindo até que a senha correta (previamente
# definida) seja inserida.

# senha = 14785

# while senha == 14785:
#     num = int(input("Insira a senha para acessar: "))
#     if num == senha:
#         print("Senha CORRETA !! PARABÉNS")
#         break
#     else:
#         print("ERROU a Senha, tente de novo")

# _____________________________________________________________           
    
# senha = 7
# tentativas = 3
# play1 = 0
# play2 = 0

# while play1 < tentativas and play1 < tentativas:
#     choice1 = int(input("Play 1 Insira um numero para ver se acertou: "))
#     play1 += 1
#     if choice1 == senha:
#         print("Play 1 VOCÊ ACERTOU!!! ")
#         break
#     else:
#         print("Errou !!!")
        
#     choice2 = int(input("Play 2 Insira um numero para ver se acertou: "))
#     play2 += 1
#     if choice2 == senha:
#         print("Play 2  TU Acertou !!!!")
#         break
#     else:
#         print("ERROU !!")
# else: 
#     print("Ninguém ACERTOU, Acabou !!!")

# _________________________________________________________

# 1 - Soma de Números Pares:
# Crie um programa que use um laço while para somar
# todos os números pares de 1 a 100 e exiba o resultado.

# x = 1

# while x < 100:
#     if x % 2 == 0:
#         print (f" {x} + {x} = {x + x }")
#     x += 1

#__________________________________________________________
#2 -
# Escreva um programa que use um laço while
# para exibir todos os números ímpares de 1 a 50.

# x = 1

# while x <= 50:
#     if x % 2 != 0 :
#         print(x)
#     x += 1

#__________________________________________________________

#3 -
# Faça um programa que use um laço while para exibir os
# primeiros 20 termos da sequência de Fibonacci.

# x = 1
# y = 0

# count = 0

# while count <= 20:
#     y , x = x, y + x
#     count += 1
#     print(y)
  
# ______________________________________________


# palavra = "Infinity"

# for i in palavra:
#     print(i)

#_______________________________________________

# 1 - Faça um programa que solicite um número ao usuário e use
# um laço for para exibir a tabuada desse número (de 1 a 10).

# num = int(input("Insira um numero para ver a Taboada até o 10: "))
# mult= 1

# for i in range (1,11):
#     if i <=10:
#         result = num * mult
#         print (f"{num} x {mult} = {result} ")
#         mult += 1
        

#_________________________________________

# 2 - Crie um programa que use um laço for para somar
# todos os números de 1 a 100 e exiba o resultado.

# x = 1
# y = 0

# for i in range (1,101):
#     if i <= 100:
#         print(f"{x} + {y} = {x + y}")
#         result = x + y
#         x += 1
#         y = result
      
# soma = 0

# for i in range(1, 101):
#     soma += i

# print(soma)

# _________________________________________________
# 3 - Faça um programa que solicite um número ao usuário e use
# um laço for para exibir a tabuada desse número (de 1 a 10).
# wor = str(input("Insira uma PALAVRA: "))

# for i in wor:
#     print(i)

# ___________________________________________________

# 4 - Desenvolva um programa que use um laço for para fazer uma
# contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".


# count = 10   Errei 

# for i in count:
#     count -= 1
#     if count == 0:
#         print ("Feliz Ano novo!!!")
    
  
# for i in range(10, -1, -1):
#     print (i)
# print("Feliz Ano NOVO !!!")
    
# ___________________________________________________


# Escreva um programa que solicite ao usuário 10 números e use um
# laço for com uma condicional para contar quantos são positivos e
# quantos são negativos.
    
# posi = 0
# neg = 0

# for i in range (1, 11):
#     num = int(input("Insira NUMEROS negativos e positivos para contarmos eles: "))
#     if num >0:
#         posi += 1
#     else:
#         neg += 1
# print ("A quantidade de Numeros negativos é: ", neg)
# print ("A quantidade de Numeros Positivos é: ", posi)

#_____________________________________________________


#Escreva um programa que use um laço for para somar 
#todos os números pares de 1 a 50 e exiba o resultado final.


# soma = 0

# for i in range (2,51,2):
#     soma += i
    

# print(soma)

#____________________________________________________

#Crie um programa que solicite uma palavra ao usuário e use um laço for com
#uma condicional para contar quantas vogais (a, e, i, o, u) a palavra contém.

# word = str(input("Insira uma PALAVRA: ")).lower()
# result = 0

# for i in word:
#     if i in "aeiou":
#         result += 1

# print(f" A palavra que você digitou tem {result} vogais ")
             
# _______________________________________________________

# Crie um algoritmo que converta uma temperatura de Celsius
# para Fahrenheit. Solicite ao usuário a temperatura em Celsius
# e exiba o resultado em Fahrenheit.

# num = float(input("Vamos converter para Fahrenheit, digite: "))

# fahr = (num * 1.8) + 32

# print(fahr)
#______________________________________________________________

# Desenvolva um programa que peça a idade do usuário e
# informe se ele é criança, adolescente, adulto ou idoso.

# num = int(input("Digite a sua idade: "))

# if num <= 11:
#     print("Você é Crianaça !")
# elif num <= 18:
#     print("Você é Adolencente !")
# elif num <= 59:
#     print("Você é Adulto!!! ")
# else:
#     print("Você é idoso!!!")

#_____________________________________________________________


#Crie um programa em Python que simule um sistema de login. O programa deve permitir ao usuário 
# três tentativas para acertar o nome de usuário e a senha corretos. Caso o usuário erre as credenciais, 
# o programa deve fornecer uma mensagem informando quantas tentativas restam. Se o usuário acertar, 
# uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.
# Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma mensagem de 
# "Acesso bloqueado" repetida três vezes.

# senha = 1478
# usuario = "chefe"
# chances = 3

# for i in range (1,4):
#     login = str(input("Digite o seu usuário: "))
#     senha2 = int(input("Digite a senha: "))
#     if login == usuario and senha2 == senha:
#         print("Acesso LIBERADO BEM VINDO CHEFE!! ")
#         break
#     else:
#         chances -= 1
#         print(f"Credenciais erradas! Você só tem mais {chances} tentativas")
#         if chances == 0:
#             print("Limite de tentativas Excedidas, ACESSO BLOQUEADO")
#             break

#______________________________________________________________________




# mix = ['jose',67, 'new york', 'fdfdgh', '59', 1500, '36', '#$*&!', 22.69]

# mix.insert(2, 'LOREN') inserir elemento na posição desejada
# mix.append("CIGARRA!")
# mix.remove('jose')
# mix.pop(6)

# print(mix)

 #____________________________________________________________________


# lista_bancos = [
# 'nubank', 'c6 bank', 'banco inter', 'banco original', 
# 'banco nomad', 'itau', 'bradesco', 'santander', 'banco do brasil',
# 'banco dacoval', 'banco safra', 'banco pine', 'banco panamericano', 'banco votorantim'
# ]


# lista_bancos[0] = 'JOSE !!!!' dessa forma ele vai mudar o elemento da posição zero.


# for i in lista_bancos:
#     print("[X]", i )
# ______________________________________________________________________



# first_tupla = ( 'jose', 'lula', 'bolsonaro', 'pamela')



# jose, lula, bolsonaro, pamela = first_tupla

# print('elem1:', jose)
# print('elem2:', lula)
# print('elem3:', bolsonaro)
# print('elem4:', pamela)

# ________________________________________________________________________
# Crie uma tupla para representar as informações de três
# palestrantes, cada uma contendo o nome, o tema da
# palestra e a instituição à qual estão vinculados.

# Exiba na tela as informações do terceiro palestrante,
# incluindo nome, tema da palestra e instituição.



# palestra_tupla = (
# ['Jose Augusto', 'FEA USP', 'Mercado Financeiro'], 
# ['Pamela', 'UNIPAM', 'Estetica'], ['Lorenzo','USP','Matematica']
# )

# #primeiro palestrante
# print('Palestrante:', palestra_tupla [0][0])
# print('Instituição:',palestra_tupla [0][1] )
# print('Tema:',palestra_tupla [0][2] )
# print('               ')
# #terceiro pelstrante
# print('Palestrante:', palestra_tupla [2][0])
# print('Instituição:',palestra_tupla [2][1] )
# print('Tema:',palestra_tupla [2][2] )

# _________________________________________________________

# Crie uma lista contendo seis frutas de sua escolha. Depois de ter a 
# lista pronta, converta essa lista em uma tupla. Por fim, exiba o conteúdo 
# da tupla resultante para verificar as frutas que foram armazenadas.

# frutas = ['manga', 'banana', 'abacate', 'laranja', 'uva','melancia']

# fruta_tupla = tuple(frutas)

# print(fruta_tupla)

# ultimo feito 19/04/2024





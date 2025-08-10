
# Aqui é um algoritimo que diz se o usuário pode dirigir ou não de acordo com a 
#idade que ele põe

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
 
###

# Aqui é um laço de repetição, onde o usuário calculo desconto em % de um produto. 

# while True:
#     precoproduto = float(input("Insira o preço do produto: "))

#     desconto = int(input('Insira o desconto em %: '))

#     valor_desc = (desconto / 100) * precoproduto

#     valor_final = precoproduto - valor_desc

#     print (f' O valor do produto sendo {precoproduto} com de desconto de {desconto}% terá um valor final de {valor_final}')

#     opção = int(input('Escolha uma opção 1 para ficar ou 2 para sair: '))

#     if opção == 1:
#         print('    Continue    ')
#     elif opção == 2:
#         print ('     Saiu !   ')
#         break


    
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

# Aqui informa se na frase tem letra B maiuscula true ou false

# frase = str(input("Escreva uma FRASE qualquer: "))

# word1 = 'b'

# if word1 in frase:
#     print("Na sua frase tem a letra B")
# else:
#     print("Sua frase não tem Letra B")

##

# num = 21

# if num > 20:
#     print("o numero é maior que 20")
# elif num > 10:
#     print("O numero é maior que 10")

##

# Verifica se a frase contém a letra 'b' ou 'B'
# e informa ao usuário a quantidade encontrada

# frase = str(input("    Escreva uma frase: "))

# wordb = frase.lower().count('b')

# print(f'    Na sua frase tem {wordb} letras B   ')




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

# ________________________________________________________________

# frutas = set()

# fru2={"maça", 'manga'}

# frutas.update(fru2)

# print(frutas)

# print('maça' in frutas)


# __________________________________________________________________

# fruts_red = {'morango', 'cereja', 'framboesa'}

# fruts_red.remove('cereja')
# fruts_red.discard('morango')

# print(fruts_red)

#___________________________________________________________________

# a = {'casa', 'fazenda', 'edificio', 'apartamento'}

# b = {'leide', 'pamela', 'jose', 'lorenzo'}

# c = a|b

# print(c)

# _____________________________________________________________________

# Crie um programa que recebe dois conjuntos e exibe a
# interseção deles.

# conjunto1 = (input("Digite os elementos do set1 separados por ponto e virgula: "))
# conjunto2 = (input("Digite os elementos do set2 separados por ponto e virgula: "))

# conj1 = set(i.strip()for i in conjunto1.split(",")) 
# conj2 = set(i2.strip()for i2 in conjunto2.split(","))

# intersessao = conj2.intersection(conj1)
 
# print(intersessao)

# _________________________________________________________________________

# dicionario = {
#     'nome': 'Jose Augusto',
#     'idade': 28 ,
#     'País' : 'Noruega',
#     'bancos' : {'clear corretora': 'ações', 'nubank': 'credit card', 'inter':{'ações', 'dolar', 'american stocks'} }
#     }

# print(dicionario['bancos']['inter'])

#___________________________________________________________________________

# Escreva um programa que EXIBA um dicionário contendo
# informações de pessoas (nome, idade) e exiba essas
# informações.

# dados = {
#     'nome': 'Jose Augusto',
#     'Idade': 33,
#     'cidade': 'São Paulo',
#     'Profissão': 'Cientista de DADOS'

# }

# dados['nome']='Pamela'
# dados['Idade'] = 32
# dados['Profissão']= 'Lash Designer'

# for i in dados.items():
#     print(i)
# _________________________________________________________________________
# Crie um dicionário que irá armazenar informações de um contato, 
# incluindo o nome, o telefone e o email. Peça ao usuário para fornecer 
# esses dados, solicitando que ele insira o nome do contato, o número de 
# telefone e o endereço de email. Após coletar todas as informações necessárias, 
# exiba o conteúdo do dicionário, mostrando todas as informações do 
# contato inserido pelo usuário.

# nome = input('Insira o seu nome: ')
# tel = input('Insira o seu tel: ')
# email = input('Insira o seu e-mail: ')

# dados = {
#     'nome': '',
#     'telefone': '',
#     'email': '',
# }

# dados['nome']=nome
# dados['telefone']=tel
# dados['email']=email


# for i in dados.items():
#     print(i)
# ___________________________________________________________

# # Versão 2 - após estudar um pouco mais

# dados = dict ()

# dados['nome'] = input("Digite o nome do contato: ")
# dados['telefone'] = input("Digite o telefone do contato: ")
# dados['email'] = input("Digite o email do contato: ")


# print (dados)
# _______________________________________________________________________


# for i in range (1, 5):
#     print (f'começando {i} Loop')

#     for y in range (5):
#         print (f'{i}º loop completo')


# ________________________________________________________________________

# produto = input('Insira uma palavra: ')


# for i in range (1,6):
#     print(f' loop {i} iniciando')

#     for i in range(3):
#         print(f'Loop {i} dentro do loop comçando')
#         for i in produto:
#             print(i)
    


# print('LOOP FINALIZADO')

# _________________________________________________________

# for i in range (1,21):
#      for i1 in range (1,11):
#          resu = i*i1
#          print(f'{i}x{i1}={resu}')
         
#          if i1 == 10:
#               i3 = i + 1
#               print(f'Agora vamos para tabuada do {i3}!')

# ___________________________________________________________
        


# def somar (a, b):
#     resu = a + b
#     return resu

# num1= 5
# num2= 11
# print(somar(num1, num2))

# def saudacao (nome):
#     print(f'Olá {nome}')

# nome = 'Pamela'

# saudacao(nome)

# def saudacao (nome, sobnome):
#     print(f'Olá {nome} {sobnome}')

# saudacao('Pamela', 'Souza')


# def saudacao (nome):
#     return f'Olá {nome}'

# nome = "Jose"
# print(saudacao(nome))

# def nome_compl(nome, sobnome):
#     return f'{nome} {sobnome}'


# apresentacao = f'Ola meu {nome_compl('Jose Augusto', 'Batista')} e tenho 33 anos'

# print(apresentacao)


# Crie uma função que receba um horário e imprima
# "Bom dia!","Boa tarde!" o "Boa noite!" conforme o horário.

# def saudacao (horario):
#     if int(horario) <= 13:
#         print('Bom dia!!!')
#     elif horario > 13 and horario <= 18:
#         print('Boa tarde')
#     elif horario > 18 and horario <= 23:
#         print('Boa Noite !!')


# while True:
#     hora = input('Digite a hora agora ou digite exit para sair: ')
#     if hora == 'exit':
#         print('BYEEEEE !')
#         break
#     else:
#         saudacao(hora)

# def saudacao (horario):
#     if 0 <= horario <= 12:
#         return 'Bom Dia!!!'
#     if 13 <= horario <= 18:
#         return 'Boa Tarde!!!'
#     if 19 <= horario <= 23:
#         return 'Boa Noite!!!'
#     else:
#         return'Hora inválida !'


# while True:
#     entrada = input('Digite a hora agora ou digite exit para sair: ')

#     if entrada.lower() == 'exit':
#         print('BYEEEEE !')
#         break

#     if not entrada.isdigit():
#         print("Por favor, digite um número válido")
#         continue
#     hora = int(entrada)
#     if hora > 23 or hora < 0:
#         print(' hora fora do existente, digite somente de 0 a 23')
#         continue
#     print(saudacao(hora))


    

# _____________________________________

# def remover_ultima_letra(*args):
#     for palavra in args:
#         print(palavra[0:-1])

# print(remover_ultima_letra
#       ("Teste", "Contexto", "Palavras", "Frase", "Argumento", "Ola"))


# def saudacao (horario):
#     if 0 <= horario <= 12:
#         return 'Bom dia !!' 
#     elif 13 <= horario <= 18:
#         return 'Bom tarde !!'
#     elif 19 <= horario <= 23:
#         return 'Boa noite !!'
#     else:
#         return 'Digite um numero VÁLIDO!! '

# while True:
#     entrada = input ('Insira um horario para receber Cumprimento: ')

#     if entrada.lower() == 'exit':
#         print('BYEEEE')
#         break
#     if not entrada.isdigit:
#         print("Digite numero válido")
#     hora = int(entrada)
#     if 0 > hora or hora > 23:
#         print(' Digite um valor de 0 a 23')
#     print(saudacao(hora))

# _____________________________________________________________

# def somar (a, b):
#     return a + b


# num = int(input('Insira o 1º numero'))
# num2 = int(input('Insira o 2º numero para somar'))


# print(somar(num, num2))

# _______________________________________________________________

# def somar (a, b):
#     return a + b

# def sub (a, b):
#     return a - b

# def mult (a, b):
#     return a * b

# def div (a, b):
#     return a / b


# while True:
#     num = int(input('Insira o 1º numero: '))
#     num2 = int(input('Insira o 2º numero: '))
#     sinal = int(input('digite 1 somar, 2 subtrair, 3 multiplicar, 4 dividir ou 5 sair: '))
#     if sinal == 1:
#         print(somar(num, num2))
#     if sinal == 2:
#         print(sub(num, num2))
#     if sinal == 3:
#         print(mult(num, num2))
#     if sinal == 4:
#         print(div(num, num2))
#     if sinal == 5:
#         print ('Saiu BYEE')
#         break
# ________________________________________________________


# def media (a, b, c):
#     d = a + b + c
#     return d / 3


# n1 = 10
# n2 = 10
# n3 = 8

# print(media(n1, n2, n3))

# ___________________________________________________________

# 09/07/2025

# REVISÃO LOGICA DE PROGRAMAÇÃO

# Desenvolva um algoritmo que calcule o preço de um produto
# após aplicar um desconto. Solicite o preço original e o percentual
# de desconto.


# contagem = 0

# while True:
    
#     produto = int(input("Digite o Valor do produto R$: "))
#     desc1 = int(input("Digite o desconto em %: "))

#     desconto = produto * (desc1/100)

#     valor= produto - desconto

#     print(f"O valor do produto é {produto} e desconto sendo de {desc1}%, então valor do produto será R${valor}")
#     contagem += 1 

#     if contagem >= 10:
#         break

# _________________________________________________________
# Algoritmo de Conversão de Tempo:
# Desenvolva um algoritmo que converta uma quantidade de
# segundos fornecida pelo usuário em horas, minutos e segundos.


# while True:

#     print('Vamos converter')
#     segundos=int(input("Digite uma quantide de segundos maior que 3600: "))

#     horas = segundos//3600

#     minuto = (segundos % 3600) // 60

#     segundos2 = segundos % 60

#     print(f' {segundos} Em horas = {horas} h {minuto} min {segundos2}s')
    


#     contin= input('Deseja continuar? S ou N: ')

#     if contin.lower() != 's': 
#         break


# _________________________________________________________________
    

    #fazer uma calculadora de multiplicação



# while True:
#     num = int(input('Digite o numero para ver a Tabuada dele: '))

#     for i in range(1,11):
#         if i < 11:
#             resu = num * i
#             print(f' {num} x {i} = {resu}')
    
#     opcao = int(input(' Digite 1 ficar ou 2 para sair: '))

#     if opcao== 1:
#         continue
#     elif opcao == 2:
#         break
# ____________________________________________________________________________    


# Crie um conjunto vazio chamado frutas e adicione as seguintes frutas a ele: 
# " maçã" , "banana " , " uva " , "laranja " e " morango ". Em seguida, imprima o conjunto.

# frutas = []

# print('antes')

# print('lista:',frutas)
# print()
# frutas.extend(["Maçã", "banana", 'uva','laranja', 'morango'] )

# print('depois')
# print('lista:',frutas)
# print()


#______________________________________________________________________

# Verifique se a fruta "banana " está presente no 
# conjunto frutas e imprima o resultado.


# saber = "banana" in frutas

# print(saber)

# # Remova a fruta " uva " do conjunto frutas_
# # vermelhas e imprima o conjunto atualizado.

# frutas.remove('uva')
# print()

# print('lista depois de removido')
# print(frutas)

# ______________________________________________________________

# ultima atualização 10/08


# Crie uma função que receba um horário e imprima "Bom dia!" , 
# "Boa tarde!" ou "Boa noite!" conforme o horário.


# def cumpri (a, b):
#     if a >= 12 and a <= 18:
#        print('Boa tarde !!!!')
#     elif a >= 19 and a <= 23 and b <= 59:
#        print ('Boa noite!!')
#     else:
#        print ('Bom dia !!')



# cumpri(10,59)



# Crie uma calculadora com opções de soma, multiplicação, 
# subtração, divisão e sair. (Ela deverá funcionar infinitamente, 
# até que o usuário decida sair da calculadora.)    

def som (a,b):
    somar = a + b
    return somar


def multi (a,b):
    multi = a * b
    return multi

def subtra (a,b):
    sub = a - b
    return sub

def div (a,b):
    divs = a / b
    return divs

while True:
    calculo = int(input('\nDigite 1 para somar, 2 multiplicar, 3 subtrair, 4 dividir: '))
    print()
    if calculo == 1:
        num1 = int (input( 'Digite um numero:'))
        print ()
        num2 = int (input('Digite outro:  '))
        print(som(num1, num2))
    elif calculo == 2:
        num1 = int (input( 'Digite um numero:'))
        print ()
        num2 = int (input('Digite outro:  '))
        print(multi(num1, num2))
    elif calculo == 3:
        num1 = int (input( 'Digite um numero:'))
        print ()
        num2 = int (input('Digite outro:  '))
        print(subtra(num1, num2))
    elif calculo == 4:
        num1 = int (input( 'Digite um numero:'))
        print ()
        num2 = int (input('\nDigite outro:  '))
        print(div(num1, num2))
    
    opcao = str(input(' \nDeseja fazer mais uma conta?  '))
    if opcao == 'sim':
        continue
    elif opcao == 'nao':
        break










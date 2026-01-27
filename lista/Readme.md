Calculadora de Média com Verificação de Aprovação

Este projeto contém um programa simples em Python que lê 5 notas do usuário, calcula a média e informa se o aluno foi Aprovado ou Reprovado com base nessa média.

O que o código faz?

1-recebe 5 notas digitadas pelo usuario
2-soma todas as notas
3-calcula a média
4-verifica se o aluno foi aprovado ou reprovado

Descrição do codigo

notas=[0,0,0,0,0]
soma=0  
x=0  
media=7

notas =lista onde sera armazenada as notas digitadas pelo usuario
soma= soma as notas inseridas
x=contador para o loop
meida=valor minimo para aprovação

while x<5:  
 notas[x]=float(input(f"nota {x+1}: "))
soma+=notas[x]
x+=1

while=o while vai de 0 a 4
notas[x]=notas inseridas pelo usuario e armazenada na lista
soma+= a nota é adicionada a soma total
x+=1 = contador para reiniciar o loop

if soma >= media:
print(f"Média: {soma/5} Aprovado")
else:
print(f"Média: {soma/5} Reprovado")

if= verifica a soma da media com o valor minimo da aprovação
else= se a soma da média for menor que o valor minimo sera exibido uma mensagem de REPROVADO

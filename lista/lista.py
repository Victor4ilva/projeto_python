notas=[0,0,0,0,0]
soma=0
x=0
media=7
while x<5:
    notas[x]=float(input(f"nota {x+1}: "))
    soma+=notas[x]
    x+=1

if soma >= media:
    print(f"Média: {soma/5} Aprovado")
else:
    print(f"Média: {soma/5} Reprovado")

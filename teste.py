'''fib1 = 0 #primeiro termo da sequencia 
fib2 = 1 #segundo termo da sequencia
num = 0 # #o valor calculado para termos maiores que 2
resposta = False #variável booleana que determina se o valor faz parte ou não da sequencia

n = int(input('Digite um número inteiro natural: ')) #recebe o valor a ser encontrado

while True: #laço de repetição responsável por calcular os valores da sequencia
    if num == n: 
        resposta = True
        break
    elif num < n:
        num = fib1 + fib2
        fib1 = fib2
        fib2 = num
    else:
        break


print()
if resposta:
    print('Faz parte')
else:
    print('Não faz parte')'''


'''import random

mes = random.choice([28, 30, 31]) #define quantos dias terão o mês
feriados = random.randint(0, 4) #define a quanditade de feriados que terão no mês

dias = list()
faturamento = list()
media = list()

maximo = 0
minimo = 1000001

cont = 0
while cont < feriados: #determina os dias da semana que terão feriados
    feri = random.randint(0, mes)
    if feri not in dias:
        dias.append(feri)
        cont += 1


for i in range(mes): #gera os faturamentos de maneira aleatória
    fat = round(random.uniform(0, 100001), 2)

    if i in dias or i in [5, 6, 12, 13, 19, 20, 26, 27]:
        faturamento.append('x')
    else:
        faturamento.append(fat)

for i in faturamento:
    if i != 'x':
        if i > maximo:
            maximo = i
        if i < minimo:
            minimo = i


i = 0
c = 0
n = 0
d = 0
while True:
    if c == 6:
        media.append(round(n/d, 2))
        c = 0
        n = 0
        d = 0
    if faturamento[i] != 'x':
        n += faturamento[i]
        d += 1
    c += 1
    i += 1
    if  i == mes:
        break




print(faturamento)
print()
print(maximo)
print()
print(minimo)
print()
print(media)'''


'''string = input('Digite a String: ')

tamanho = len(string)-1
reverso = ''

for i in range(tamanho, -1, -1):
    reverso += string[i]

print(reverso)'''


'''faturamento = dict()

faturamento['SP'] = 67836.43
faturamento['RJ'] = 36678.66
faturamento['MG'] = 29229.88
faturamento['ES'] = 27165.48
faturamento['Outros'] = 19849.53

total = 0

for i in faturamento.keys():
    total += faturamento[i]

print(total)'''

k = 0 
soma = 0
i = 13

while k < i:
    k += 1
    soma += k

print(soma)
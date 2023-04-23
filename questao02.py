fib1 = 0 #primeiro termo da sequencia 
fib2 = 1 #segundo termo da sequencia
num = 0 # #o valor calculado para termos maiores que 2
resposta = False #variável booleana que determina se o valor faz parte ou não da sequencia

n = int(input('Digite um número inteiro natural: ')) #recebe o valor a ser encontrado

while True: #laço de repetição responsável por calcular os valores da sequencia
    if num == n: #verifica se o valor faz parte da sequencia
        resposta = True
        break
    elif num < n: #verifica se o elemento ainda pode fazer parte da sequência
        num = fib1 + fib2
        fib1 = fib2
        fib2 = num
    else: #o elemento não faz parte da sequência
        break


print()
if resposta:
    print('Faz parte')
else:
    print('Não faz parte')

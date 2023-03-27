""" 
Q01 - Qual será o valor da variável SOMA? """

def calcular_soma():
    INDICE = 13
    SOMA = 0
    K = 0
    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K
    print(f"Resposa Q01: {SOMA}")
calcular_soma()


###############################################################################################################################
""" 
Q02 - Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva uma função em python que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. """

def pertence_fibonacci(n):
    if n == 0 or n == 1:
        return True
    
    a, b = 0, 1
    
    # realiza a iteração para gerar a sequência até encontrar um valor maior ou igual a n
    while b < n:
        a, b = b, a + b
    
    # verifica se n é igual a b (se pertence à sequência) e retorna True ou False
    return n == b

# Sequência de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34..
print(pertence_fibonacci(0))  
print(pertence_fibonacci(1))  
print(pertence_fibonacci(21))  
print(pertence_fibonacci(2))  
print(pertence_fibonacci(6))  


###############################################################################################################################
""" 
3) Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, ___

b) 2, 4, 8, 16, 32, 64, ____

c) 0, 1, 4, 9, 16, 25, 36, ____

d) 4, 16, 36, 64, ____

e) 1, 1, 2, 3, 5, 8, ____

f) 2,10, 12, 16, 17, 18, 19, ____ """

#Solução Q03a
def prox_elemento_a(seq):
    return seq[-1] + 2
print("Resposta 3a: ", prox_elemento_a([1, 3, 5, 7]))  # 9
#Solução Q03b
def prox_elemento_b(seq):
    return seq[-1] * 2
print("Resposta 3b: ", prox_elemento_b([2, 4, 8, 16, 32, 64]))  # 128
#Solução Q03c
def prox_elemento_c(seq):
    n = len(seq) + 1
    return (n-1)**2
print("Resposta 3c: ", prox_elemento_c([0, 1, 4, 9, 16, 25, 36]))  # 49
#Solução Q03d
def prox_elemento_d(seq):
    n = len(seq) + 1
    return (n*2)**2
print("Resposta 3d: ", prox_elemento_d([4, 16, 36, 64]))  # 100
#Solução Q03e
def prox_elemento_e(seq):
    n = len(seq) + 1
    if n == 1 or n == 2:
        return 1
    else:
        return seq[-1] + seq[-2]
print("Resposta 3e: ", prox_elemento_e([1, 1, 2, 3, 5, 8]))  # 13
#Solução Q03f
def prox_elemento_f(seq):
    if seq[-1] < 19:
        return seq[-1] + 2
    else:
        return seq[-1] + 1
print("Resposta 3f: ", prox_elemento_f([2, 10, 12, 16, 17, 18, 19]))  # 20



###############################################################################################################################

def mais_proximo_ribeirao():
    # Distância total percorrida pelo carro até o encontro
    dist_carro = 110/60 * 54.5 # km

    # Distância total percorrida pelo caminhão até o encontro
    dist_caminhao = 80/60 * 75 # km

    # Distância restante do carro até Ribeirão Preto
    dist_restante_carro = 50 # km

    # Distância restante do caminhão até Franca
    dist_restante_caminhao = 100 - 50 # km

    if dist_restante_carro < dist_restante_caminhao:
        return "O carro está mais próximo de Ribeirão Preto."
    else:
        return "O caminhão está mais próximo de Ribeirão Preto."

print(mais_proximo_ribeirao()) # O carro está mais próximo de Ribeirão Preto.



###############################################################################################################################
""" 
Q05 -Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse; """

def inverte_string(string = 'analise e desenvolvimento'):
    return string[::-1]

print(inverte_string())
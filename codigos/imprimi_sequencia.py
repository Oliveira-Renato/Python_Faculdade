def imprimeLinha(x):
    for n in range(1, x + 1):
        print(('  {} ').format(n), end='')
    print()

def imprimeSequencia(num):
    for a in range(num + 1):
        imprimeLinha(a)
        
numero = input('Digite um número: ')
imprimeSequencia(int(numero))
imprimeSequencia(4)
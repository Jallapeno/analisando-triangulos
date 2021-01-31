# Calculando a condição de existência de um triângulo

print("""\nNão é qualquer conjunto de três medidas que é capaz de formar um triângulo. 
Para que isso ocorra, é preciso que seja respeitada a chamada condição de existência, 
que diz que a medida de qualquer um dos lados do triângulo tem que ser menor do que a 
soma das medidas dos outros dois e, ainda, maior que a diferença entre elas.\n""")

print('Exemplo: A = 3, B = 4 e C = 5 podem formar um triângulo.\nCaso A = 3, B = 4 e C = 8 não formará triângulo nenhum!\n')

a = int(input('Informe o valor do lado A: '))
b = int(input('Informe o valor do lado B: '))
c = int(input('Informe o valor do lado C: '))

# A linha abaixo representa o método matemático clássico para esta análise
# if (b - c < a < b + c) and (a - c < b < a + c) and (a - b < c < a + b):

# A linha abaixo representa o método prático de realizar essa análise
if a < b + c and b < a + c and c < a + b:
    print('\nOs valores informados podem formar um triângulo.')
else:
    print('\nOs valores informados não podem formar um triângulo!\n')
    print("""Se a soma for menor que a medida maior, essas medidas não podem formar um triângulo. 
Por um simples motivo: a linha reta é a menor distância entre dois pontos, portanto, 
o lado do triângulo é a menor distância entre aqueles dois vértices.\n
A soma dos outros dois lados formam um desvio, portanto tem que ser maior do que o lado em si, 
que é a menor distância entre aqueles pontos. Se o caminho do desvio é menor que a linha reta, 
esse triângulo não existe.""")

print('\nReferências: https://www.stoodi.com.br/blog/matematica/triangulo/')

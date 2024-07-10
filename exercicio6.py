"""

Crie um programa que peça ao usuário três números (pode ser decimal ou inteiro) e calcule a média desses números. 
O programa deve exibir a média com duas casas decimais. Salve como "exercicio6.py"

"""

# receba do usúario um número e armazena
varNumero1 = float(input("Digite um número: "))

# receba do usúario um número e armazena
varNumero2 = float(input("Digite um número: "))

# receba do usúario um número e armazena
varNumero3 = float(input("Digite um número: "))

#calcula a média entre os números
varMedia = (varNumero1 + varNumero2 + varNumero3) / 3

#exibe o resultado com duas casas decimais 
print(f'A média é {varMedia:.2f}.')



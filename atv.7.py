# ETE PORTO DIGITAL
# LPC - Introdução a Python
# Prof. Cloves Rocha
# Estudante: Elisa Vitória
# Turma: 1°B

#7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

l = float(input('Qual o valor do lado do quadrado? '))
a = l**2
a2 = a * 2
print('O dobro da área do quadrado é \033[36m{}\033[m.' .format(a2))
# ETE PORTO DIGITAL
# LPC - Introdução a Python
# Prof. Cloves Rocha
# Estudante: Elisa Vitória
# Turma: 1°B

#6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

r = float(input('Qual o valor do raio? '))
pi = 3.14
a = pi * r **2
print('A área é \033[7m{}\033[m.' .format(a))
# ETE PORTO DIGITAL
# LPC - Introdução a Python
# Prof. Cloves Rocha
# Estudante: Elisa Vitória
# Turma: 1°B

#8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

rh = float(input('Quanto você recebe por hora? '))
htm = float(input('Quantas horas você trabalha por mês? '))
s = rh * htm
print('seu salário no mês é de \033[32m{}\033[m.'.format(s))
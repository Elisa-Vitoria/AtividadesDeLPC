# ETE PORTO DIGITAL
# LPC - Introdução a Python
# Prof. Cloves Rocha
# Estudante: Elisa Vitória
# Turma: 1°B

#9. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

n = float(input('Digite um número: '))
if n > 0:
   print('O número \033[34m{}\033[m é positivo'.format(n))
elif n == 0:
   print('O número \033[37m{}\033[m é neutro'.format(n))
else:
   print('O número \033[31m{}\033[m é negativo'.format(n))

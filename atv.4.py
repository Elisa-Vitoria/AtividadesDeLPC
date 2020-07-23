# ETE PORTO DIGITAL
# LPC - Introdução a Python
# Prof. Cloves Rocha
# Estudante: Elisa Vitória
# Turma: 1°B

#4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

n1 =  float(input('digite sua primeira nota: '))
n2 =  float(input('digite sua segunda nota: '))
n3 =  float(input('digite sua terceira nota: '))
n4 =  float(input('digite sua quarta nota: '))
m = (n1+n2+n3+n4)/(4)
print('Sua média é \033[1:30m{}\033[m.' .format(m))
# ETE PORTO DIGITAL
# LPC - Introdução a Python
# Prof. Cloves Rocha
# Estudante: Elisa Vitória
# Turma: 1°B

#11. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input('Digite uma letra: '))
if letra in 'aeiou':
   print('A letra \033[34m{}\033[m é uma vogal.'.format(letra))
else:
   print('A letra \033[36m{}\033[m é uma consoante.'.format(letra))
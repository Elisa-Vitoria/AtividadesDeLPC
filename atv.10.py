# ETE PORTO DIGITAL
# LPC - Introdução a Python
# Prof. Cloves Rocha
# Estudante: Elisa Vitória
# Turma: 1°B

#10. Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input('Digite seu sexo com F ou M: '))
if sexo == 'F':
   print('\033[31m{}\033[m é do sexo feminino.'.format(sexo))
elif sexo == 'M':
   print('\033[34m{}\033[m é do sexo masculino.'.format(sexo))
else:
   print('O \033[1:30m{}\033[m sexo digitado é inválido.'.format(sexo))
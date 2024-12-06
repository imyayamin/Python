#Faça um Programa que verifique se uma letra digitada é vogal ou consoante

import string 
x = input ("Digite uma letra:")

if x in string.ascii_letters: /*verifica se é uma letra*/

  if x.upper() in 'AEIOU':
    print ("Vogal")

  else:
    print('Consoante')

else: 
  print ('Não é uma letra')

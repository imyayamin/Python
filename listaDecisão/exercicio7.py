#Faça um Programa que leia três números e mostre o maior e o menor deles.

x = int(input("Digite o primeiro numero: "))
y = int(input("Digite o segundo numero: "))
z = int(input("Digite o terceiro numero: "))

if x > y and x > z:
  print('O maior numero é:' , x )

elif y > x and y > z:
  print('O maior numero é:' , y)

else:
  print('O maior numero é:' , z)


if x < y and x < z:
  print('O menor numero é:' , x)

elif y < x and y < z:
  print('O menor numero é:' , y)

else:
  print('O menor numero é:' , z)
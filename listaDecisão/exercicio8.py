#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

x = float(input("Digite o preço do primeiro produto: "))
y = float(input("Digite o preço do segundo produto: "))
z = float(input("Digite o preço do terceiro produto: "))

if x < y and x < z:
  print("O primeiro produto é o mais barato, com o valor de: ", {x})

elif y < x and y < z:
  print(f"O segundo produto é o mais barato, com o valor de: {y}")

elif z < x and z < y:
  print(f"O terceiro produto é o mais barato, com o valor de: {z}")

else:
  print("Os valores dos produtos são iguais")

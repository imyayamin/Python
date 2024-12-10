#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que deve calcular os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

inicial = float(input("Digite o salário do colaborador:"))

if inicial <= 280.00:
  percentual = 20
  
elif inicial <= 700.00:
  percentual = 15

elif inicial <= 1500.00:
  percentual = 10

else:
  percentual = 5

aumento = inicial * percentual / 100
novoSalario = inicial + aumento

print("Salario inicial: ", inicial)
print("Percentual de aumento: ", percentual)
print("Valor do aumento: ", aumento)
print("Novo salário: ", novoSalario)
  

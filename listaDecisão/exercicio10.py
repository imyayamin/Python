#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("Digite o turno em que você estuda (M-matutino, V-Vespertino)")

match turno:
  case "M":
    print("Bom dia!")

  case "V":
    print("Boa tarde!")

  case "N":
    print("Boa noite!")

  case _:
    print("Valor inválido!")

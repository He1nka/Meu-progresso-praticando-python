print("Vamos descobrir qual é sua operadora pelo seu código!")
operadoras = str(input("Qual o código da sua operadora (C, V, T OU O)?:"))

if operadoras == "C":
  print("Sua operadora é Claro")

elif operadoras == "V":
  print("Sua operadora é Vivo")

elif operadoras == "T":
  print("Sua operadora é Tim")

elif operadoras == "O":
  print("Sua operadora é Oi")

else:
  print("Operadora não encontrada")
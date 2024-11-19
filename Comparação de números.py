print(f"Seja bem vindo!"
  f"\nVamos comparar os números digitados.")

valor1 = int(input(f"Digite o primeiro número: "))
valor2 = int(input(f"Digite o segundo número: "))


if valor1 > valor2:
  print(f"O primeiro número é maior que o segundo número")
elif valor1 < valor2:
  print(f"O segundo número é maior que o primeiro número")
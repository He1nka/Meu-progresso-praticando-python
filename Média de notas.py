print("Digite o valor das suas notas")

nota1 = float(input(print("Digite o valor da primeira nota:")))
nota2 = float(input(print("Digite o valor da segunda nota:")))
media =  (nota1 + nota2) / 2

if media >= 7:
    print("sua média foi:",media,"você foi aprovado")
elif media <= 4:    
    print("sua média foi:",media, "Você foi reprovado")
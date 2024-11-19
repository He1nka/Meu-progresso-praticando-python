# Programa que retorna o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.

salario_mensal = input("Digite seu salário mensal:")
horas_trabalhadas_por_mes = input("Digite suas horas trabalhadas:")
valor_hora = int(salario_mensal) / int(horas_trabalhadas_por_mes)
print("Voce ganha R$:", valor_hora, "por hora")
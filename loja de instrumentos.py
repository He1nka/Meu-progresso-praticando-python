print("Bem vindo a nossa loja de instrumentos!") 
operadoras = str(input("Diga o código do instrumento (G, B, P OU V)?:")) 

if operadoras == "P": 
  print("Você escolheu o pandeiro, que custa 200 reais.") 
elif operadoras == "V": 
  print("Você escolheu o violão, que custa 800 reais ") 
elif operadoras == "B": 
  print("Você escolheu o Bateria, que custa 3000 reais ") 
elif operadoras == "G": 
  print("Você escolheu a guitarra, que custa 1000 reais") 
else: 
  print("Instrumento não encontrado") 
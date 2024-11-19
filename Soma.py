print(f"Seja bem vindo!"f"\nVamos somar e comparar os números digitados.") 

número1 = int(input("Digite um número:"))
número2 = int(input("Digite outro número:"))
    
print("A soma desses números resulta em:", número1 + número2)

print("Agora vamos comparar esse resultado com outro número!")

número3 = int(input("Digite mais um número:"))

if número1 + número2 > número3:
    print("Este número é menor do que a soma")
elif número1 + número2 < número3:
    print("Este número é maior do que a soma")
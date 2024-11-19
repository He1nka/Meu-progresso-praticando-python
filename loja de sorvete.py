sorveteChoVenda = float(input("quantos litros foram vendidos?"))
sorveteBauVenda = float(input("quantos litros foram vendidos?"))
sorveteFloVenda = float(input("quantos litros foram vendidos?"))
sorveteCocoVenda = float(input("quantos litros foram vendidos?"))
sorveteTapVenda = float(input("quantos litros foram vendidos?"))
sorveteMenVenda = float(input("quantos litros foram vendidos?"))

sorveteChoEstoque = float(input("quantos litros tem no estoque?")),
sorveteBauEstoque = float(input("quantos litros tem no estoque?")),
sorveteFloEstoque = float(input("quantos litros tem no estoque?")),
sorveteCocoEstoque = float(input("quantos litros tem no estoque?")),
sorveteTapEstoque = float(input("quantos litros tem no estoque?")),
sorveteMenEstoque = float(input("quantos litros tem no estoque?"))


quantidadelitrosvendas = sorveteChoVenda + sorveteBauVenda + sorveteFloVenda + sorveteCocoVenda + sorveteTapVenda + sorveteMenVenda
print(quantidadelitrosvendas)

quantidadelitrosestoque = sorveteChoEstoque + sorveteBauEstoque + sorveteFloEstoque + sorveteCocoEstoque + sorveteTapEstoque + sorveteMenEstoque
print(quantidadelitrosestoque)

mediadelitrosvenda = (quantidadelitrosvendas) / 6
print(mediadelitrosvenda)

mediadelitrosestoque = (quantidadelitrosestoque) / 6
print(mediadelitrosestoque)

print("RECIBO")
cliente = input("Digite seu nome: ")
produto = input("Você irá abastecer com (E) etanol ou (G) gasolina? ")
litros = (float(input(f"Quantos litros de você vai abastecer? ")))


if produto == "E" or produto == "e":
    resultado = litros *  4.10
    print(f"O {cliente} abasteceu com etanol o total foi:{resultado}")
elif produto == "G" or produto == "g":
    resultado = litros * 5.8
    print(f"O {cliente} abasteceu com gasolina o total foi:{resultado}")
else:
    print("invalido")
print("Tabela de Produtos")
print("----------------------------")
print("Código | Produto        | Preço")
print("1      | Cachorro Quente| R$ 4.00")
print("2      | X-Salada       | R$ 4.50")
print("3      | X-Bacon        | R$ 5.00")
print("4      | Torrada simples| R$ 2.00")
print("5      | Refrigerante   | R$ 1.50")
print("----------------------------")


codigo = int(input("digite o codigo do produto desejado "))
quantidade = int(input("digite a quantidade do seu produto "))



if codigo == 1:
    preco = 4.00
elif codigo == 2:
    preco = 4.50
elif codigo == 3:
    preco = 5.00
elif codigo == 4:
    preco = 2.00
elif codigo == 5:
    preco = 1.50

total = preco * quantidade

print(f"Total: R${total}")


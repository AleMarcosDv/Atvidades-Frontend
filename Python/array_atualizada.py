
print("Bem vindos á Noboticário!!!")

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'shampoos', 'sabonetes', 'delineadores']

lista_produtos[1] = "rímel"
lista_produtos[4] = "cremes hidratantes"
lista_produtos.pop()
lista_produtos.append("base")
lista_produtos.append("acetona")

for i in range(len(lista_produtos)):
  print("Nós temos", lista_produtos[i], "à venda")
from sanduiche1 import Lanche 
from cardapio import Cardapio

resposta = 's'
# Cirando o objeto da classe cardapio fora do laço
c = Cardapio
while resposta == 's':

    ingredientes = []
    nome = input("Nome do sanduíche: ")
    preco = float(input("Preço do sanduíche: "))
    qtdeIngredientes = int(input("Escreva quantos ingredientes você quer adicionar: "))
    for i in range(qtdeIngredientes):
        ingrediente = input(f"Informe o ingrediente: {i+1}:")
        ingredientes.append(ingrediente)
        
    # Criando o objeto da classe Lanche dentro laço
    l = Lanche(nome,preco,ingredientes)
            
    # Adicionando o lanche "1" ao cardápio "c"
    c.adicionarItem(l)
    resposta = input("Deseja adicionar outro item ao cardápio? (s/n)")

# Fim do laço while

c.exibirCardapio()
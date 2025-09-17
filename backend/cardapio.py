from sanduiche1 import Lanche
class Cardapio:
    def __init__(self):
        self.itens = []
        self.categoria = ""
    # Fim do construtor

    def __str__(self):
        return f"Item: {self.itens}"; 

    # Criação do método adicionar item
    def adicionarItem(self,item: Lanche):
        """
        Adicionar um objeto (item)  da classe Lanche ao cardápio
        """
        self.itens.append(item)
    # Fim do método adicionarItem

    def exibirCardapio(self):
        for item in self.itens:
            item.exibirLanche()
# Fim da classe

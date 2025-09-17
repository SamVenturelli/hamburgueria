class Lanche:
    def __init__( self, nome, preco, ingredientes):
        self.nome = nome
        self.preco = preco
        self.ingredientes = ingredientes
    # fim do construtor __init__()

    def exibirLanche(self):
        """
        Exibe os dados do lanche cadastrado (nome, preco e ingredientes[])
        """
        print(f"Sanduíche:{self.nome}; Preço:{self.preco}; Ingredientes:{self.ingredientes}")

#fim da classe




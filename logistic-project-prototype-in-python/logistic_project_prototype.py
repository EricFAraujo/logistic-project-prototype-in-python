class Produto:
    def __init__(self, nome, data_validade, estoque):
        self.nome = nome
        self.data_validade = data_validade
        self.estoque = estoque

    def registrar_saida(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            print(f"{quantidade} unidades de {self.nome} foram retiradas do estoque.")
        else:
            print("Quantidade insuficiente em estoque.")

    def mostrar_estoque(self):
        print(f"Produto: {self.nome}")
        print(f"Data de Validade: {self.data_validade}")
        print(f"Estoque atual: {self.estoque}")

def main():
    produtos = []

    while True:
        print("\nMenu:")
        print("1. Cadastrar novo produto")
        print("2. Registrar saída de produto")
        print("3. Mostrar estoque")
        print("4. Adicionar mais produtos")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            data_validade = input("Digite a data de validade: ")
            estoque = int(input("Digite a quantidade em estoque: "))
            produtos.append(Produto(nome, data_validade, estoque))
            print("Produto cadastrado com sucesso!")

        elif opcao == "2":
            nome_produto = input("Digite o nome do produto: ")
            quantidade_saida = int(input("Digite a quantidade de saída: "))
            produto_encontrado = False
            for produto in produtos:
                if produto.nome == nome_produto:
                    produto.registrar_saida(quantidade_saida)
                    produto_encontrado = True
                    break
            if not produto_encontrado:
                print("Produto não encontrado.")

        elif opcao == "3":
            for produto in produtos:
                produto.mostrar_estoque()

        elif opcao == "4":
            nome = input("Digite o nome do produto: ")
            data_validade = input("Digite a data de validade: ")
            estoque = int(input("Digite a quantidade de estoque: "))
            novo_produto = Produto(nome, data_validade, estoque)
            produtos.append(novo_produto)
            inserir_produto:(novo_produto)
            print("Produto adicionado com sucesso!")

        elif opcao == "5":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Escolha uma opção válida.")

if __name__ == "__main__":
    main()


import os

opcao = 0

while opcao != 5:
    print("------ MENU -----")
    print("1 - Cadastrar produto")
    print("2 - Listar todos produtos")
    print("3 - Consultar produto por linha")
    print("4 - Excluir produto por linha")
    print("5 - Sair")

    opcao = int(input("Escolha a opção: "))

    if opcao == 1:
        print("\n--- CADASTRAR PRODUTO ---")

        codigo = input("Digite o código do produto: ")
        produto = input("Digite o nome do produto: ")
        preco = input("Digite o preço do produto: ")
        quantidade = input("Digite a quantidade do produto: ")

        arquivo = open("produtos.txt", "a")
        arquivo.write(f"{codigo},{produto},{preco},{quantidade}\n")
        arquivo.close()

        print("\nProduto cadastrado com sucesso!")
        input("Pressione ENTER para continuar...")
        os.system("cls")

    elif opcao == 2:
        print("\n--- LISTAR TODOS OS PRODUTOS ---\n")

        arquivo = open("produtos.txt", "r")
        linhas = arquivo.readlines()
        arquivo.close()

        contador = 1

        for linha in linhas:
            codigo, produto, preco, quantidade = linha.strip().split(",")

            print(f"Linha:       {contador}")
            print(f"Código:      {codigo}")
            print(f"Produto:     {produto}")
            print(f"Preço:       {preco}")
            print(f"Quantidade:  {quantidade}")
            print("--------------------------\n")

            contador = contador + 1

        input("Pressione ENTER para continuar...")
        os.system("cls")

    elif opcao == 3:
        print("\n--- CONSULTAR PRODUTO POR LINHA ---\n")

        arquivo = open("produtos.txt", "r")
        linhas = arquivo.readlines()
        arquivo.close()

        numero_linha = int(input("Digite o número da linha que deseja consultar: "))

        linha = linhas[numero_linha - 1]

        codigo, produto, preco, quantidade = linha.strip().split(",")

        print("\n--- PRODUTO ENCONTRADO ---")
        print(f"Linha:       {numero_linha}")
        print(f"Código:      {codigo}")
        print(f"Produto:     {produto}")
        print(f"Preço:       {preco}")
        print(f"Quantidade:  {quantidade}")
        print("--------------------------\n")

        input("Pressione ENTER para continuar...")
        os.system("cls")

    elif opcao == 4:
        print("\n--- EXCLUIR PRODUTO POR LINHA ---\n")

        arquivo = open("produtos.txt", "r")
        linhas = arquivo.readlines()
        arquivo.close()

        contador = 1

        for linha in linhas:
            codigo, produto, preco, quantidade = linha.strip().split(",")

            print(f"Linha:       {contador}")
            print(f"Código:      {codigo}")
            print(f"Produto:     {produto}")
            print(f"Preço:       {preco}")
            print(f"Quantidade:  {quantidade}")
            print("--------------------------\n")

            contador = contador + 1

        remover = int(input("Digite o número da linha que deseja excluir: "))

        remover = remover - 1

        linhas.pop(remover)

        arquivo = open("produtos.txt", "w")

        for linha in linhas:
            arquivo.write(linha)

        arquivo.close()

        print("\nProduto removido com sucesso!")
        input("Pressione ENTER para continuar...")
        os.system("cls")

    elif opcao == 5:
        print("Saindo do sistema...")

    else:
        print("Opção inválida.")
        input("Pressione ENTER para continuar...")
        os.system("cls")
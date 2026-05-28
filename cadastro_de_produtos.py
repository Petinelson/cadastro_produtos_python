import os

opcao = 0

while opcao != 5:
    print("------ MENU -----")
    print("1 - Cadastrar produto")
    print("2 - Listar todos produtos")
    print("3 - Consultar produto por linha")
    print("4 - Excluir produto por linha")
    print("5 - Sair")

    try:
        opcao = int(input("Escolha a opção: "))
    except ValueError:
        print("\nErro: Por favor, digite um número válido para a opção.")
        input("Pressione ENTER para continuar...")
        os.system("cls")
        continue

    if opcao == 1:
        print("\n--- CADASTRAR PRODUTO ---")

        codigo = input("Digite o código do produto: ")
        produto = input("Digite o nome do produto: ")
        preco = input("Digite o preço do produto: ")
        quantidade = input("Digite a quantidade do produto: ")

        try:
            # Apenas garantindo que o arquivo possa ser aberto sem problemas
            arquivo = open("produtos.txt", "a")
            arquivo.write(f"{codigo},{produto},{preco},{quantidade}\n")
            arquivo.close()
            print("\nProduto cadastrado com sucesso!")
        except Exception as e:
            print(f"\nErro ao salvar o produto: {e}")

        input("Pressione ENTER para continuar...")
        os.system("cls")

    elif opcao == 2:
        print("\n--- LISTAR TODOS OS PRODUTOS ---\n")

        try:
            arquivo = open("produtos.txt", "r")
            linhas = arquivo.readlines()
            arquivo.close()

            if not linhas:
                print("Nenhum produto cadastrado ainda.")
            else:
                contador = 1
                for linha in linhas:
                    # O try interno evita que uma linha corrompida quebre a listagem inteira
                    try:
                        codigo, produto, preco, quantidade = linha.strip().split(",")
                        print(f"Linha:        {contador}")
                        print(f"Código:       {codigo}")
                        print(f"Produto:      {produto}")
                        print(f"Preço:        {preco}")
                        print(f"Quantidade:   {quantidade}")
                        print("--------------------------\n")
                    except ValueError:
                        print(f"Linha {contador}: Erro nos dados desta linha (formato inválido).")
                        print("--------------------------\n")
                    
                    contador = contador + 1
        except FileNotFoundError:
            print("O arquivo 'produtos.txt' ainda não existe. Cadastre um produto primeiro.")

        input("Pressione ENTER para continuar...")
        os.system("cls")

    elif opcao == 3:
        print("\n--- CONSULTAR PRODUTO POR LINHA ---\n")

        try:
            arquivo = open("produtos.txt", "r")
            linhas = arquivo.readlines()
            arquivo.close()

            if not linhas:
                print("Nenhum produto cadastrado ainda.")
            else:
                numero_linha = int(input("Digite o número da linha que deseja consultar: "))
                
                # Valida se o número da linha é positivo e existe na lista
                if numero_linha <= 0 or numero_linha > len(linhas):
                    print("\nErro: Esta linha não existe no arquivo.")
                else:
                    linha = linhas[numero_linha - 1]
                    codigo, produto, preco, quantidade = linha.strip().split(",")

                    print("\n--- PRODUTO ENCONTRADO ---")
                    print(f"Linha:        {numero_linha}")
                    print(f"Código:       {codigo}")
                    print(f"Produto:      {produto}")
                    print(f"Preço:        {preco}")
                    print(f"Quantidade:   {quantidade}")
                    print("--------------------------\n")

        except FileNotFoundError:
            print("O arquivo 'produtos.txt' ainda não existe. Cadastre um produto primeiro.")
        except ValueError:
            print("\nErro: Digite um número inteiro válido para a linha ou formato da linha inválido.")

        input("Pressione ENTER para continuar...")
        os.system("cls")

    elif opcao == 4:
        print("\n--- EXCLUIR PRODUTO POR LINHA ---\n")

        try:
            arquivo = open("produtos.txt", "r")
            linhas = arquivo.readlines()
            arquivo.close()

            if not linhas:
                print("Nenhum produto cadastrado para excluir.")
            else:
                contador = 1
                for linha in linhas:
                    try:
                        codigo, produto, preco, quantidade = linha.strip().split(",")
                        print(f"Linha:        {contador}")
                        print(f"Código:       {codigo}")
                        print(f"Produto:      {produto}")
                        print(f"Preço:        {preco}")
                        print(f"Quantidade:   {quantidade}")
                        print("--------------------------\n")
                    except ValueError:
                        print(f"Linha {contador}: [Linha corrompida]")
                        print("--------------------------\n")
                    
                    contador = contador + 1

                remover = int(input("Digite o número da linha que deseja excluir: "))

                if remover <= 0 or remover > len(linhas):
                    print("\nErro: Linha inválida. Nenhuma alteração foi feita.")
                else:
                    remover = remover - 1
                    linhas.pop(remover)

                    arquivo = open("produtos.txt", "w")
                    for linha in linhas:
                        arquivo.write(linha)
                    arquivo.close()

                    print("\nProduto removido com sucesso!")

        except FileNotFoundError:
            print("O arquivo 'produtos.txt' ainda não existe. Cadastre um produto primeiro.")
        except ValueError:
            print("\nErro: Digite um número inteiro válido para a exclusão.")

        input("Pressione ENTER para continuar...")
        os.system("cls")

    elif opcao == 5:
        print("Saindo do sistema...")

    else:
        print("Opção inválida.")
        input("Pressione ENTER para continuar...")
        os.system("cls")

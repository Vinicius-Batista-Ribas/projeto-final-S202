from cli import CLI
op = CLI()

while True:
    print("*"*10)
    print("1. Adicionar Jogo")
    print("2. Atualizar Jogo")
    print("3. Remover Jogo")
    print("4. Listar Jogos")
    print("5. Adicionar Categoria")
    print("6. Atualizar Categoria")
    print("7. Remover Categoria")
    print("8. Listar Categorias")
    print("9. Associar Jogo a Categoria")
    print("10. Remover Associação de Jogo")
    print("11. Listar Associações")
    print("0. Sair")
    print("*"*10)
    escolha = input("Escolha uma opção: ")

    if escolha not in [str(i) for i in range(14)]:
        print("opcao invalida")

    if escolha == "0":
        break
    elif escolha == "1":
        op.adicionar_jogo()
    elif escolha == "2":
        op.atualizar_jogo()
    elif escolha == "3":
        op.remover_jogo()
    elif escolha == "4":
        op.listar_jogos()

    elif escolha == "5":
        op.adicionar_categoria()
    elif escolha == "6":
        op.atualizar_categoria()
    elif escolha == "7":
        op.remover_categoria()
    elif escolha == "8":
        op.listar_categorias()

    elif escolha == "9":
        op.associar_jogo_categoria()
    elif escolha == "10":
        op.remover_associacao_jogo_categoria()
    elif escolha == "11":
        op.listar_associacoes()
"""
É o menu principal do jogo. Server para chamar as funções menu 
"""


class MenuPrincipal:

    def menu_principal_ficha(self):

        # IMPORTS
        import os

        # VARIÁVEIS
        validador_menu = True
        pergunta_sair = ""

        # MOSTRA O MENU DE OPÇÕES DO MENU PRINCIPAL
        while validador_menu:
            os.system("cls")
            opcao_menu = input(
                "\n\nMENU PRINCIPAL\nDigite uma das  opções a seguir:\n\n"
                "[1] ATRIBUTOS\n"
                "[2] SUBATRIBUTOS\n"
                "[3] VANTAGENS\n"
                "[4] DESVANTAGENS\n"
                "[5] PERÍCIAS\n"
                "[6] INFORMAÇÕES EXTRAS\n"
                "[7] PRINTAR A FICHA\n"
                "[8] SALVAR FICHA\n"
                "[9] CARREGAR UMA FICHA EXISTENTE\n"
                "[0] SAIR\n\n"
                "Selecionar:"
            )

            # 1 - ATRIBUTOS
            if opcao_menu == "1":
                from menu_atributo import Atributos

                menu_atributos = Atributos()
                menu_atributos.menu_atributos()  # Chamar função que chama o menu de atributos
                validador_menu = False

            # 2 - SUBATRIBUTOS
            elif opcao_menu == "2":
                ...  # Chamar função equivalente

            # 3 - VANTAGENS
            elif opcao_menu == "3":
                ...

            # 4 - DESVANTAGENS
            elif opcao_menu == "4":
                ...

            # 5 - PERÍCIAS
            elif opcao_menu == "5":
                from menu_pericia import Pericias

                menu_pericias = Pericias()
                menu_pericias.menu_pericias()

            # 6 - INFORMAÇÕES EXTRAS
            elif opcao_menu == "6":
                ...
            # 7 - PRINTAR A FICHA
            elif opcao_menu == "7":
                ...

            # 8 - SALVAR FICHA
            elif opcao_menu == "8":
                ...
            # 9 - CARREGAR UMA FICHA EXISTENTE
            elif opcao_menu == "9":
                ...

            # 0 - SAIR
            elif opcao_menu == "0":
                pergunta_sair = input(
                    "\n\nTem certeza que deseja sair?\n Digite [s] para sair."
                )
                if pergunta_sair.lower() == "s":
                    print("\n\nSAINDO DO PROGRAMA\n\n")
                    validador_menu = False
                else:
                    continue

            # DIGITAR UMA OPÇÃO INVÁLIDA
            else:
                print(
                    "Desculpe. Você não digitou uma opção válida\n"
                    "Digite um dos valores do menu sem digitar os []."
                )

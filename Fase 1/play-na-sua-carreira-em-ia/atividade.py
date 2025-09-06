usuario_loggado = True
culturas_disponiveis = ["Café", "Soja"]
opcoes_do_menu = ["1 - Calcular area de plantio", "2 - Calcular manejo de insumos", "3 - Alterar dados da cultura",  "4 - Escolher outra cultura", "5 - Sair"]
cultura_selecionada = None
dados_da_cultura = []
opcao_selecionada = None

while(usuario_loggado):
    # esta area é um retangulo
    def calcular_area_cultura_cafe():
        area_da_cultura = (dados_da_cultura[0] * dados_da_cultura[1])
        return print(f"A area da cultura do Café é de: {area_da_cultura} metros.")

    # esta area é um triangulo
    def calcular_area_cultura_soja():
        area_da_cultura = (dados_da_cultura[0] * dados_da_cultura[1]) / 2
        return print(f"A area da cultura da Soja é de: {area_da_cultura} metros.")

    #Nitrogênio: 80 a 150 kg/ha
    #Fósforo (P2O5): 40 a 100 kg/ha
    #Potássio (K2O): 80 a 150 kg/ha
    def aplicar_macronutrientes_cafe():
        area_da_aplicacao = dados_da_cultura[0] * dados_da_cultura[1]
        total_insumos = (150 + 100 + 150) * area_da_aplicacao # usar um for aqui e calcular separado
        print(f"O total de macronutrientes a serem aplicados é de: {total_insumos}kg")

    # 8.000 metros cúbicos de água por hectare    
    def irrigar_soja():
        area_da_irrigacao = (dados_da_cultura[0] * dados_da_cultura[1]) / 2
        total_insumos = 8000 * area_da_irrigacao
        print(f"O total de agua a ser gasta na irrigacao é de: {total_insumos} metros cubicos.")  

    def editar_dados_da_cultura():
        for indice, dado in enumerate(dados_da_cultura):
            match indice:
                case 0:
                    dados_da_cultura[indice] = (int(input(f"Digite a nova base da regiao da plantacao em metros ou pressione enter para manter o valor anterior de {dado}: ")))  
                case 1:
                    dados_da_cultura[indice] = (int(input(f"Digite a nova largura da regiao da plantacao em metros ou pressione enter para manter o valor anterior de {dado}: ")))
    
    if(cultura_selecionada is None):
        print("Opçoes de culturas:\n")
        for indice, cultura in enumerate(culturas_disponiveis):
            print(f"{indice} - {cultura}")
        try:
            cultura_selecionada = int(input("Digite uma opcao de cultura e pressione Enter para continuar: "))
            if(cultura_selecionada < 0 or cultura_selecionada > 1):
                raise ValueError()
            dados_da_cultura.append(int(input("Digite a base da regiao da plantacao em metros: ")))
            dados_da_cultura.append(int(input("Digite a largura da plantacao em metros: ")))
        except ValueError:
            print("Por favor digite uma opcao de cultura valida. \n")
            cultura_selecionada = None
            dados_da_cultura = []
            continue

    if(opcao_selecionada is None):
        print(f"Menu de cultura do {culturas_disponiveis[cultura_selecionada]}:\n")
        for opcao in opcoes_do_menu:
            print(opcao)
        try:
            opcao_selecionada = int(input("\nDigite uma opção do menu acima e pressione Enter para continuar: "))
        except ValueError:
            print("\nOpcao inválida. \n")
            opcao_selecionada = None
    else:
        match opcao_selecionada:
            case 1:
                # 0 cafe - 1 soja depois mudamos
                if(cultura_selecionada == 0):
                    calcular_area_cultura_cafe()
                else:
                    calcular_area_cultura_soja()
            case 2:
                if(cultura_selecionada == 0):
                    aplicar_macronutrientes_cafe()
                else:
                    irrigar_soja(0)
            case 3:
                editar_dados_da_cultura()
            case 4:
                dados_da_cultura = []
                cultura_selecionada = None
            case 5:
                usuario_loggado = False
            case _:
                print("Opção inválida. \n")
        opcao_selecionada = None

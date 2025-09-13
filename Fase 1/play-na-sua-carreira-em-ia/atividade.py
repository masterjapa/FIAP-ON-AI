usuario_loggado = True
culturas_disponiveis = ["Café", "Soja"]
opcoes_do_menu = ["1 - Calcular area de plantio", "2 - Calcular manejo de insumos", "3 - Alterar dados da cultura",  "4 - Escolher outra cultura", "5 - Sair"]
cultura_selecionada = None
# 0 - data da operacao, 1 - ano da safra, 2 - comprimento, 3 - largura, 4 - espaçamento entre plantas
dados_da_cultura = []
opcao_selecionada = None
manejo_de_insumos = None
area_da_aplicacao_do_manejo = None

while(usuario_loggado):
    def exportar_dados():
        try:
            nome_do_arquivo = "dados_da_coleta.csv"
            nome_da_cultura = culturas_disponiveis[cultura_selecionada]
            dados_a_serem_convertidos: list = [nome_da_cultura] + dados_da_cultura + [area_da_aplicacao_do_manejo] + [manejo_de_insumos] +  ["\n"]
            dados_da_cultura_convertidos = map(str,  dados_a_serem_convertidos)
            dados_a_serem_salvos = ", ".join(dados_da_cultura_convertidos)
            with open(nome_do_arquivo, "a", encoding="utf8") as f:
                f.write(dados_a_serem_salvos)
                print("Dados salvos com sucesso!!!\n")
        except Exception as e:
            print("Erro ao exportar.", e)

    def calcular_area_cultura():
        # 0 cafe - 1 soja
        if(cultura_selecionada == 0):
            return calcular_area_cultura_cafe()
        else:
            return calcular_area_cultura_soja()  
    # esta area é um retangulo
    def calcular_area_cultura_cafe():
        area_da_cultura = (dados_da_cultura[2] * dados_da_cultura[3])
        print(f"A area da cultura do Café é de: {area_da_cultura} hectares.")
        return area_da_cultura

    # esta area é um triangulo
    def calcular_area_cultura_soja():
        area_da_cultura = (dados_da_cultura[2] * dados_da_cultura[3]) / 2
        print(f"A area da cultura da Soja é de: {area_da_cultura} hectares.")
        return area_da_cultura
    
    def calcular_manejo_de_insumos(area_da_aplicacao_do_manejo: float):
        if(cultura_selecionada == 0):
            return aplicar_macronutrientes_cafe(area_da_aplicacao_do_manejo)
        else:
            return irrigar_soja(area_da_aplicacao_do_manejo)

    #Nitrogênio: 80 a 150 kg/ha
    #Fósforo (P2O5): 40 a 100 kg/ha
    #Potássio (K2O): 80 a 150 kg/ha
    # metodo trator
    def aplicar_macronutrientes_cafe(area_da_aplicacao: float):
        total_insumos = (150 + 100 + 150) * area_da_aplicacao
        print(f"O total de macronutrientes a serem aplicados é de: {total_insumos}kg")
        return total_insumos

    # 8.000 hectares cúbicos de água por hectare    
    def irrigar_soja(area_da_irrigacao: float):
        total_insumos = 8000 * area_da_irrigacao
        print(f"O total de agua a ser gasta na irrigacao é de: {total_insumos} hectares cubicos.")
        return total_insumos
    
    def coletar_dados_cultura():
            dados_da_cultura.append(str(input("Insira a data da operacao no formato DD/MM/AAAA: ")))
            dados_da_cultura.append(int(input("Insira o ano da safra: ")))
            dados_da_cultura.append(float(input("Insira o comprimento da plantacao em hectares: ")))
            dados_da_cultura.append(float(input("Insira a largura da plantacao em hectares: ")))
            dados_da_cultura.append(float(input("Insira o espaçamento entre plantas em metros: ")))
            print("\n")

    def editar_dados_da_cultura():
        print("Para manter o dado anterior pressione Enter.")
        # 0 - data da operacao, 1 - ano da safra, 2 - comprimento, 3 - largura, 4 - espaçamento entre plantas
        for indice, dado in enumerate(dados_da_cultura):
            match indice:
                case 0:
                    dados_da_cultura[indice] = (str(input(f"Insira a nova data da operacao: ") or dado))
                case 1:
                    dados_da_cultura[indice] = (int(input(f"Insira o novo ano da safra: ") or dado))                    
                case 2:
                    dados_da_cultura[indice] = (float(input(f"Insira o novo comprimento da plantacao em hectares: ") or dado))
                case 3:
                    dados_da_cultura[indice] = (float(input(f"Insira a nova largura da regiao da plantacao em hectares: ") or dado))
                case 4:
                    dados_da_cultura[indice] = (float(input(f"Insira o novo espaçamento entre plantas em metros: ") or dado))
                     
    
    if(cultura_selecionada is None):
        print("Opçoes de culturas:\n")
        for indice, cultura in enumerate(culturas_disponiveis):
            print(f"{indice} - {cultura}")
        try:
            cultura_selecionada = int(input("Digite uma opcao de cultura e pressione Enter para continuar: "))
            if(cultura_selecionada < 0 or cultura_selecionada > 1):
                raise ValueError()
            coletar_dados_cultura()
        except ValueError:
            print("Por favor digite um valor válido. \n")
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
                area_da_aplicacao_do_manejo = calcular_area_cultura()
            case 2:
                if area_da_aplicacao_do_manejo is None:
                    area_da_aplicacao_do_manejo = calcular_area_cultura()
                manejo_de_insumos = calcular_manejo_de_insumos(area_da_aplicacao_do_manejo)
                exportar_dados()
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

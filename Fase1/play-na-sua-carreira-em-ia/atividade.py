from datetime import datetime, timedelta

usuario_loggado = True
culturas_disponiveis = ["Café ☕", "Soja 🫘"]
opcoes_do_menu = [
    "\n=== Menu Principal ===\n"
    "1 - Calcular área de plantio 🌱",
    "2 - Calcular manejo de insumos 💧",
    "3 - Previsão da colheita 📅",
    "4 - Estimativa de lucro 💰",
    "5 - Estimativa de colheita em kg 📦",
    "6 - Ruas de lavoura 🚜",  
    "7 - Alterar dados da cultura ✏️",
    "8 - Escolher outra cultura 🔄",
    "9 - Sair ❌"
]   
cultura_selecionada = None
dados_da_cultura = []
opcao_selecionada = None

while(usuario_loggado):
         
    def calcular_area_cultura_cafe():
        area_da_cultura = (dados_da_cultura[0] * dados_da_cultura[1])
        res_a_cafe = f"☕ ÁREA DA CULTURA DO CAFÉ: {area_da_cultura} m² ☕"
        borda = "■" * len(res_a_cafe)
        print("\n" + borda)
        print(res_a_cafe)
        print(borda + "\n")

    def calcular_area_cultura_soja():
        area_da_cultura = (dados_da_cultura[0] * dados_da_cultura[1]) / 2
        csoja = f"🌱 ÁREA DA CULTURA DO SOJA: {area_da_cultura} m² 🌱"
        borda = "■" * len(csoja)
        print("\n" + borda)
        print(csoja)
        print(borda + "\n")

    def aplicar_macronutrientes_cafe():
        area_da_aplicacao = dados_da_cultura[0] * dados_da_cultura[1]
        total_insumos = (150 + 100 + 150) * area_da_aplicacao # usar um for aqui e calcular separado
        res_macro = f"💊 TOTAL DE MACRONUTRIENTES: {total_insumos} kg 💊"
        borda = "■" * len(res_macro) #len retorna o tamanho 
        print("\n" + borda)
        print(res_macro)
        print(borda + "\n") 

    def irrigar_soja():
        area_da_irrigacao = (dados_da_cultura[0] * dados_da_cultura[1]) / 2
        total_insumos = 8000 * area_da_irrigacao
        irr = f"💧 O TOTAL DE ÁGUA A SER GASTA NA IRRIGAÇÃO É DE: {total_insumos} m³ 💧"
        borda = "■" * len(irr)
        print("\n" + borda)
        print(irr)
        print(borda + "\n")

    def previsao_colheita():
        try:
            data_plantio_str = input("📅 Digite a data do plantio (dd/mm/aaaa): ")
            cultura = cultura_selecionada  
            if cultura == 0:  
                ciclo = 200
            else: 
                ciclo = 120
            data_plantio = datetime.strptime(data_plantio_str, "%d/%m/%Y") #converte a string em  datetime
            data_colheita = data_plantio + timedelta(days=ciclo)
            pc = f"🌱 Previsão de colheita: {data_colheita.strftime('%d/%m/%Y')}\n"
            borda = "■" * len(pc)
            print("\n" + borda)
            print(pc)
            print(borda + "\n")

        except ValueError:
            print("⚠️ Data inválida. Digite no formato dd/mm/aaaa.\n")          

    def estimativa_lucro():

        if not dados_da_cultura:
            print("⚠️ Primeiro escolha uma cultura e defina a área.\n")
            return
        try:
            area = dados_da_cultura[0] * dados_da_cultura[1]  # base * largura
            rendimento = float(input("Digite o rendimento médio por m² (kg/m²): "))
            preco = float(input("Digite o preço de venda por kg: R$ "))
            custo_total = float(input("Digite o custo total da plantação: R$ "))
            quantidade_colhida = area * rendimento
            receita = quantidade_colhida * preco
            lucro = receita - custo_total
            borda = "■" * 40
            print("\n" + borda)
            print(f"\n💰 Receita estimada: R$ {receita:.2f}")
            print(f"💸 Custos: R$ {custo_total:.2f}")
            print(f"✅ Lucro estimado: R$ {lucro:.2f}\n")
            print(borda + "\n")

        except ValueError:
            print("⚠️ Digite apenas números válidos.\n")


    def estimativa_colheita():
        if not dados_da_cultura:
            print("⚠️ Primeiro escolha uma cultura e defina a área.\n")
            return

        try:
            area = dados_da_cultura[0] * dados_da_cultura[1]
            rendimento = float(input("Rendimento médio por m² (kg/m²): "))
            quantidade_colhida = area * rendimento
            ec = f"\n📦 Estimativa de colheita: {quantidade_colhida:.2f} kg\n"
            borda = "■" * len(ec)
            print("\n" + borda)
            print(ec)
            print(borda + "\n")

        except ValueError:
            print("⚠️ Digite apenas números válidos.\n")


    def ruas_de_lavoura():
        if not dados_da_cultura:
            print("⚠️ Primeiro escolha uma cultura e defina a área.\n")
            return
        try:
            largura_rua = float(input("Informe a largura de cada rua (em metros): "))
            comprimento = dados_da_cultura[0]
            largura = dados_da_cultura[1]
            qtd_ruas = int(largura // largura_rua)
            total_metros = qtd_ruas * comprimento
            borda = "■" * 40
            print("\n" + borda)
            print(f"\n🚜 Número de ruas: {qtd_ruas}")
            print(f"📏 Comprimento total das ruas: {total_metros:.2f} metros\n")
            print(borda + "\n")


        except ValueError:
            print("⚠️ Digite apenas números válidos.\n")
          
    def editar_dados_da_cultura():
        for indice, dado in enumerate(dados_da_cultura):
            match indice:
                case 0:
                    dados_da_cultura[indice] = (int(input(f"Digite a nova base da regiao da plantacao em metros ou pressione enter para manter o valor anterior de {dado}: ")))  
                case 1:
                    dados_da_cultura[indice] = (int(input(f"Digite a nova largura da regiao da plantacao em metros ou pressione enter para manter o valor anterior de {dado}: ")))


    if(cultura_selecionada is None):
        print("\n🌱 Opções de culturas disponíveis 🌱")
        print("-" * 40)
        for indice, cultura in enumerate(culturas_disponiveis):
            print(f"{indice} - {cultura}")
        try:
            print("-" * 40)
            cultura_selecionada = int(input("Digite uma opção de cultura e pressione Enter para continuar: "))
            if(cultura_selecionada < 0 or cultura_selecionada > 1):
                raise ValueError()
            dados_da_cultura.append(int(input("\n📏 Digite a base da região da plantação (em metros): ")))
            dados_da_cultura.append(int(input("\n📐 Digite a largura da plantação (em metros): ")))

        except ValueError:
            print("Por favor digite uma opcao de cultura valida. \n")
            cultura_selecionada = None
            dados_da_cultura = []
            continue

    if(opcao_selecionada is None):

        print(f"\nMenu de cultura do {culturas_disponiveis[cultura_selecionada]}:\n")
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
                    irrigar_soja()
            case 3:
                previsao_colheita()
            case 4:
                estimativa_lucro()        
            case 5:
                estimativa_colheita()
            case 6:
                ruas_de_lavoura()           
            case 7:
                editar_dados_da_cultura()
            case 8:
                dados_da_cultura = []
                cultura_selecionada = None
            case 9:
                usuario_loggado = False
            case _:
                print("Opção inválida. \n")
        opcao_selecionada = None

# carregar o arquivo csv
# sanitizar os dados -> preencher valores vazios ou excluir linhas que nao possam ser usadas
# calcular a media 
# calcular o desvio padrao
# imprimir os dados de media e desvio padrao

install.packages(c("dplyr", "mice", "readr"))
library("readr")
library("dplyr")
library("mice")

dados_da_coleta <- read_csv("~/Pessoal/FIAP/FIAP-ON-AI/Fase 1/play-na-sua-carreira-em-ia/dados_da_coleta.csv")
dados_da_coleta_inputados <- mice(dados_da_coleta, method="pmm")
dados_da_coleta_completos <- complete(dados_da_coleta_inputados, 1)

# aqui deixamos essas variaveis de exemplo pois poderiamos tambem filtrar os dados desejados pra depois calcular dados
cultura_cafe <- dados_da_coleta_completos %>% filter(cultura == "Café")
cultura_soja <- dados_da_coleta_completos %>% filter(cultura == "Soja")

# calculo de dados totalizados
media_manejo_de_insumos_gastos <- mean(dados_da_coleta_completos$manejo_insumos)
desvio_padrao_de_insumos_gastos <- sd(dados_da_coleta_completos$manejo_insumos)

print(media_manejo_de_insumos_gastos)
print(desvio_padrao_de_insumos_gastos)

# calculo de dados por cultura usando group_by e summarise
media_manejo_de_insumos_gastos_por_cultura <- dados_da_coleta_completos %>% group_by(cultura) %>% summarise(media_insumos = mean(manejo_insumos))
desvio_padrao_manejo_de_insumos_por_cultura <- dados_da_coleta_completos %>% group_by(cultura) %>% summarise(desvio_padrao = sd(manejo_insumos))

print(media_manejo_de_insumos_gastos_por_cultura)
print(desvio_padrao_manejo_de_insumos_por_cultura)

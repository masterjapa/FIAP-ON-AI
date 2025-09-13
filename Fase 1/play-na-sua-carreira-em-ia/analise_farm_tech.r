# carregar o arquivo csv
# sanitizar os dados -> preencher valores vazios ou excluir linhas que nao possam ser usadas
# calcular a media 
# calcular o desvio padrao
# imprimir os dados de media e desvio padrao

install.packages("dplyr")
library("dplyr")

dados_da_coleta <- read.csv("dados_da_coleta.csv", encoding="UTF-8")

cultura_cafe <- dados_da_coleta %>% filter(cultura == "Café")
cultura_soja <- dados_da_coleta %>% filter(cultura == "Soja")


install.packages("httr")
library("httr")

open_meteo_url <- "https://archive-api.open-meteo.com/v1/archive";

# latitude e longitude de MG, parametros de temperatura maxima, temperatura minima, precipitacao por hora e o periodo da analise(start e end date) -< ano 2024
parametros <-"latitude=-8.9667&longitude=-72.7833&daily=temperature_2m_max%2Ctemperature_2m_min&hourly=precipitation&start_date=2024-01-01&end_date=2024-12-31"

url_final <- paste(open_meteo_url, "?", parametros, sep="")

resposta_api <- httr::GET(url_final)
resposta_formatada <- httr::content(resposta_api, as = "text")
dados_metereologicos <- jsonlite::fromJSON(resposta_formatada)

print(dados_metereologicos)

temperatura_maxima_media_no_periodo <- mean(dados_metereologicos$daily$temperature_2m_max)
temperatura_minima_media_no_periodo <- mean(dados_metereologicos$daily$temperature_2m_min)
precipitacao_media_no_periodo <- mean(dados_metereologicos$hourly$precipitation)

print(temperatura_maxima_media_no_periodo)
print(temperatura_minima_media_no_periodo)
print(precipitacao_media_no_periodo)

# a resposta da API pode demorar um pouco pra ser processada pois estamos consumindo 1 ano de dados
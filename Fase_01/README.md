# CardioIA — Fase 1: Batimentos de Dados

**Aluno:** Diego Filipe Pereira de Araujo — RM567064
**Curso:** Bacharelado em Inteligência Artificial — FIAP ON (2º ano)
**Entrega:** Fase 1 — levantamento e preparação das bases de dados

---

## Sobre o projeto

O **CardioIA** é uma plataforma digital que simula o ecossistema de uma cardiologia moderna, construída ao longo das 7 fases do curso. Ela integrará dados clínicos, Machine Learning, Visão Computacional, IoT e agentes inteligentes para apoiar triagem, diagnóstico, monitoramento e assistência remota.

Esta primeira fase não treina modelos: ela monta o **laboratório**. O papel aqui é o de cientista de dados hospitalar, responsável por localizar, organizar e justificar as três bases que alimentarão os módulos das fases seguintes.

Três critérios guiaram toda a curadoria:

1. **Dados reais**, não simulados — o projeto trata de saúde, e conclusões sobre dados inventados não têm valor clínico.
2. **Fonte citável**, com DOI ou repositório institucional — para que qualquer pessoa possa auditar a origem.
3. **Licença aberta e explícita** — todas as três bases são CC BY 4.0 ou Open Access.

| Parte | Base | Volume | Licença |
|---|---|---|---|
| 1 — Numérica (IoT) | UCI Heart Disease, subconjunto Cleveland | 303 registros × 15 variáveis | CC BY 4.0 |
| 2 — Textual (NLP) | 2 artigos científicos brasileiros (SciELO) | ~84.500 palavras | CC BY 4.0 / Open Access |
| 3 — Visual (VC) | ECG Images dataset of Cardiac Patients (Mendeley) | 128 imagens amostradas de 928 | CC BY 4.0 |

---

## Parte 1 — Dados Numéricos (IoT)

### Origem

**São dados reais.** Trata-se do subconjunto *Cleveland* do **UCI Heart Disease Data Set**, coletado na **Cleveland Clinic Foundation** (Ohio, EUA) pelo Dr. Robert Detrano e doado ao repositório da Universidade da Califórnia em Irvine em 1988. É a base de referência da literatura de aprendizado de máquina aplicado à cardiologia — usada em centenas de artigos publicados —, o que permite comparar os resultados do CardioIA com um histórico consolidado.

- **Fonte:** https://archive.ics.uci.edu/dataset/45/heart+disease
- **Licença:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Arquivo preparado:** [`dados/cardioia_pacientes.csv`](dados/cardioia_pacientes.csv) — 303 linhas, 15 colunas
- **Link público (Google Drive):** [pasta `dados`](https://drive.google.com/drive/folders/1jPdA8cZuBwcydyPc8F6SHNlUeifP-DFM?usp=drive_link)

### Dicionário de variáveis

| Variável | Significado | Tipo / unidade |
|---|---|---|
| `age` | Idade | anos (29–77) |
| `sex` | Sexo | 1 = masculino, 0 = feminino |
| `cp` | Tipo de dor torácica | 1 = angina típica · 2 = angina atípica · 3 = dor não anginosa · 4 = assintomático |
| `trestbps` | Pressão arterial em repouso | mm Hg (94–200) |
| `chol` | Colesterol sérico | mg/dl (126–564) |
| `fbs` | Glicemia de jejum > 120 mg/dl | 1 = sim, 0 = não |
| `restecg` | Resultado do ECG em repouso | 0 = normal · 1 = anormalidade ST-T · 2 = hipertrofia ventricular |
| `thalach` | Frequência cardíaca máxima atingida | bpm (71–202) |
| `exang` | Angina induzida por exercício | 1 = sim, 0 = não |
| `oldpeak` | Depressão do segmento ST no exercício | mm |
| `slope` | Inclinação do segmento ST no pico | 1 = ascendente · 2 = plana · 3 = descendente |
| `ca` | Vasos principais corados na fluoroscopia | 0–3 |
| `thal` | Cintilografia com tálio | 3 = normal · 6 = defeito fixo · 7 = defeito reversível |
| `num` | Diagnóstico original | 0 = ausência · 1–4 = grau de obstrução |
| `doenca_cardiaca` | **Alvo binário derivado** (`num > 0`) | 0 = sem doença, 1 = com doença |

### Variáveis mais relevantes clinicamente

Nem toda coluna carrega o mesmo peso diagnóstico. As seis abaixo são as que mais importam para um modelo de IA em cardiologia:

| Variável | Por que é decisiva |
|---|---|
| `cp` — dor torácica | É a **queixa que leva o paciente ao pronto-socorro** e o primeiro filtro de qualquer triagem. Distinguir angina típica de dor não anginosa muda toda a conduta. Paradoxalmente, o valor "assintomático" também é crítico: identifica o infarto silencioso, que passa despercebido justamente por não doer. |
| `thalach` — FC máxima | Mede a **reserva funcional do coração** sob esforço. Uma frequência máxima baixa indica que o miocárdio não consegue responder à demanda, sinal clássico de isquemia. |
| `oldpeak` — depressão ST | É a **evidência eletrocardiográfica objetiva** da isquemia, medida em milímetros. Diferente da dor, não depende do relato do paciente — é dado instrumental, e por isso menos sujeito a viés de percepção. |
| `ca` — vasos obstruídos | Vem da fluoroscopia e indica **quantas artérias coronárias estão comprometidas**. É o mais próximo de uma medida direta da gravidade anatômica da doença. |
| `trestbps` e `chol` | Hipertensão e dislipidemia são os **fatores de risco modificáveis** de maior peso. São exatamente as variáveis sobre as quais uma intervenção preventiva pode agir — o que interessa a um sistema que quer prever antes de tratar. |

Além do poder preditivo, essas variáveis têm uma qualidade prática que importa para as próximas fases: `age`, `sex`, `trestbps`, `chol`, `thalach` e `fbs` são **coletáveis por sensores vestíveis ou exames de rotina**, sem cateterismo. Um módulo de triagem do CardioIA que dependesse de `ca` só funcionaria dentro do hospital; um que use as seis primeiras pode rodar em telemedicina.

### Preparação aplicada

O script [`scripts/preparar_dados.py`](scripts/preparar_dados.py) baixa a base direto do UCI, aplica os nomes de coluna do dicionário oficial, converte os marcadores `?` em campos vazios e cria o alvo binário `doenca_cardiaca`.

**O que deliberadamente não foi feito:** imputação de faltantes, normalização e criação de novas features. A Fase 1 é de coleta — tratar os dados agora esconderia decisões que precisam ser discutidas quando os modelos forem construídos.

Perfil da base preparada:

- **303 pacientes**, sendo 164 sem doença (54%) e 139 com doença (46%) — classes bem equilibradas
- Idade média de **54,4 anos**, variando de 29 a 77
- **6 valores ausentes** no total: 4 em `ca` e 2 em `thal`, ambos exames de imagem

---

## Parte 2 — Dados Textuais (NLP)

Os dois textos estão versionados em [`assets/`](assets/) e foram extraídos dos PDFs originais pelo script [`scripts/extrair_textos.py`](scripts/extrair_textos.py). Cada `.txt` traz no cabeçalho título, fonte, DOI e licença, para que a procedência viaje junto com o conteúdo.

| Arquivo | Publicação | Volume |
|---|---|---|
| [`texto_01_estatistica_cardiovascular_brasil_2023.txt`](assets/texto_01_estatistica_cardiovascular_brasil_2023.txt) | **Estatística Cardiovascular – Brasil 2023** — Arquivos Brasileiros de Cardiologia, v. 121, n. 2, 2024. Sociedade Brasileira de Cardiologia. DOI [10.36660/abc.20240079](https://doi.org/10.36660/abc.20240079) | ~80.200 palavras |
| [`texto_02_fatores_risco_cardiovascular.txt`](assets/texto_02_fatores_risco_cardiovascular.txt) | **Frequência de fatores de risco cardiovascular em voluntários participantes de evento de educação em saúde** — Revista da Associação Médica Brasileira, v. 55, n. 5, 2009. DOI [10.1590/S0104-42302009000500028](https://doi.org/10.1590/S0104-42302009000500028) | ~4.200 palavras |

Os dois foram escolhidos por serem **complementares em escala**: o primeiro é um panorama epidemiológico nacional, com dados oficiais do Ministério da Saúde e do projeto Global Burden of Disease; o segundo é um estudo de campo com pacientes concretos. Juntos, dão ao modelo tanto vocabulário estatístico-populacional quanto vocabulário clínico-individual — e ambos em **português brasileiro**, o que é essencial, já que modelos de NLP médico treinados em inglês erram com a terminologia usada no SUS.

### Como o NLP explorará esses textos

| Técnica | Aplicação no CardioIA |
|---|---|
| **Reconhecimento de entidades nomeadas (NER)** | Extrair automaticamente sintomas, fármacos, comorbidades e fatores de risco do texto corrido. É o que permitirá transformar uma anamnese escrita em campos estruturados — conectando a Parte 2 de volta à Parte 1. |
| **Classificação de tópicos** | Rotular trechos por tema (prevenção, diagnóstico, tratamento, epidemiologia) para que o agente de assistência remota recupere só o trecho pertinente à pergunta do paciente. |
| **Sumarização automática** | Condensar as 80 mil palavras da Estatística Cardiovascular em resumos executivos, apoiando a decisão clínica sem exigir leitura integral. |
| **Análise de sentimento / polaridade** | Aplicada não ao artigo, mas ao relato do paciente em fases futuras: distinguir queixas de urgência de relatos de rotina é o que permite priorizar uma fila de triagem. |

### Por que isso é relevante

A maior parte da informação clínica existente **não está em tabelas** — está em prontuários, laudos, encaminhamentos e literatura. Um sistema de IA em saúde que só lê números enxerga uma fração do que o médico enxerga. O NLP é a ponte entre esses dois mundos: é ele que transforma o texto livre em algo que o modelo da Parte 1 consegue consumir.

---

## Parte 3 — Dados Visuais (VC)

### Origem

**ECG Images dataset of Cardiac Patients**, produzido no **Ch. Pervaiz Elahi Institute of Cardiology** (Multan, Paquistão) com o eletrocardiógrafo **EDAN SE-3**. São eletrocardiogramas reais de 12 derivações, digitalizados a partir dos laudos impressos, com a grade milimetrada e o cabeçalho do exame preservados.

- **Fonte:** https://data.mendeley.com/datasets/gwbz3fsgp8/2 — DOI [10.17632/gwbz3fsgp8.2](https://doi.org/10.17632/gwbz3fsgp8.2)
- **Licença:** CC BY 4.0
- **Base completa:** 928 imagens JPEG, 615 MB, em 4 classes
- **Amostra preparada:** **128 imagens** — 32 por classe, baixadas por [`scripts/baixar_imagens.py`](scripts/baixar_imagens.py)
- **Formato verificado:** JPEG RGB, 2213 × 1572 px, 200 DPI, ~700 KB por arquivo (87 MB no total)
- **Link público (Google Drive):** [pasta `imagens_ecg`](https://drive.google.com/drive/folders/1frAroUpYGg2X7ZSsoFDV3kY5PpJHRlgp?usp=drive_link)

| Classe | Prefixo do arquivo | Base completa | Amostra |
|---|---|---:|---:|
| Pessoa normal | `Normal` | 284 | 32 |
| Batimento anormal (arritmia) | `HB` | 233 | 32 |
| Infarto agudo do miocárdio | `MI` | 239 | 32 |
| Histórico prévio de infarto | `PMI` | 172 | 32 |
| **Total** | | **928** | **128** |

A amostra pega 32 de cada classe em ordem alfabética, o que a torna reproduzível e mantém as quatro classes com o mesmo peso. Como a base de origem já é razoavelmente equilibrada, o balanceamento custa pouco: nenhuma classe precisou ser truncada de forma agressiva.

Optou-se por ECG e não por raio-X torácico porque o eletrocardiograma é o **exame cardiológico de primeira linha**: barato, rápido, disponível em qualquer UBS e diretamente ligado às variáveis `restecg`, `oldpeak` e `slope` da Parte 1. As três bases falam da mesma coisa.

### Como a Visão Computacional analisará essas imagens

| Etapa | O que acontece |
|---|---|
| **Pré-processamento** | Conversão para tons de cinza, binarização e remoção da grade milimetrada rosa de fundo, isolando o traçado da tinta do papel. |
| **Recorte do cabeçalho** | As imagens trazem no topo um cabeçalho textual com dados do exame. Ele precisa ser removido antes do treino — tanto por privacidade quanto porque a rede aprenderia a ler o texto em vez de interpretar o traçado. |
| **Segmentação das derivações** | Separação das 12 derivações (I, II, III, aVR, aVL, aVF, V1–V6) em imagens independentes — cada uma observa o coração de um ângulo elétrico diferente e precisa ser analisada isoladamente. |
| **Detecção de bordas e contornos** | Filtros como Canny e Sobel delineiam a curva do traçado, permitindo localizar o complexo QRS e medir amplitudes e intervalos entre picos. |
| **Classificação por CNN** | Uma rede convolucional aprende os padrões que separam as quatro classes — a supradesnivelação do segmento ST no infarto, a irregularidade dos intervalos R-R na arritmia, a onda Q patológica no infarto antigo. |
| **Detecção de anomalias** | Modelos treinados apenas em ECGs normais sinalizam qualquer traçado fora do padrão, cobrindo condições raras que não estão entre as quatro classes rotuladas. |

As imagens trazem no rodapé os parâmetros de aquisição (`25mm/s`, `10mm/mV`), o que é uma vantagem prática: a escala é conhecida e constante, permitindo converter pixels em milissegundos e milivolts sem calibração manual.

### Por que isso é relevante

Milhões de ECGs são feitos por ano no Brasil e, na atenção básica, a leitura frequentemente depende de um profissional sem especialização em cardiologia. Um modelo de visão computacional que faça a **pré-triagem do traçado** não substitui o cardiologista — ele ordena a fila, apontando quais exames precisam ser vistos primeiro. Em infarto agudo, cada minuto de antecipação no diagnóstico é músculo cardíaco preservado.

---

## Governança de Dados e Viés

O enunciado pede atenção à governança desde a coleta. Três pontos foram tratados explicitamente:

### Licenciamento e atribuição

As três bases são **CC BY 4.0 ou Open Access**, o que autoriza uso e redistribuição mediante citação da fonte. Nenhuma exigiu solicitação de acesso ou termo de confidencialidade. As referências completas, com DOI, estão ao final deste documento — a atribuição é a contrapartida da licença, não uma formalidade.

### Privacidade

A base numérica e os textos estão **anonimizados na origem**: não há nomes, documentos nem números de prontuário — apenas atributos clínicos e demográficos.

**As imagens são a exceção, e isso merece registro.** Ao inspecionar os arquivos baixados, verificou-se que o cabeçalho impresso em cada ECG contém um **número de identificação do exame, o sexo do paciente e a data e hora exatas da aquisição** — todos gravados nos pixels da imagem. São pseudoidentificadores: isoladamente não revelam quem é a pessoa, mas em conjunto com o registro interno da instituição de origem permitiriam reidentificação. Por isso o recorte do cabeçalho, descrito na Parte 3, é uma exigência de privacidade antes de ser uma decisão técnica. Enquanto as imagens circularem completas, elas devem ser tratadas como dado pseudonimizado, não anonimizado. Na terminologia da **LGPD (Lei 13.709/2018)**, dados de saúde são dados pessoais sensíveis (art. 5º, II) e recebem proteção reforçada — mas dados anonimizados deixam de ser dados pessoais (art. 12), o que é o que permite este uso acadêmico. Nas próximas fases, se o CardioIA passar a receber dados de pacientes reais, essa premissa muda completamente e exigirá base legal e consentimento próprios.

### Vieses identificados

Declarar os vieses agora é mais barato do que descobri-los depois de treinar um modelo:

| Base | Viés | Consequência prática |
|---|---|---|
| Cleveland | **68% dos pacientes são homens** (206 de 303) | A doença coronariana se manifesta de forma diferente em mulheres, com mais sintomas atípicos. Um modelo treinado aqui tende a subdiagnosticar mulheres. |
| Cleveland | **Coleta de 1988, hospital único nos EUA** | Critérios diagnósticos, exames e perfil populacional mudaram em quase 40 anos. Não representa a população brasileira, sua distribuição étnica nem a realidade do SUS. |
| Cleveland | **Viés de seleção** | São pacientes que já chegaram a um centro de referência em cardiologia — não a população geral. A prevalência de 46% observada não é a prevalência real. |
| ECG Mendeley | **Instituição única, aparelho único** | Todos os 928 exames vêm de um só serviço em Multan, no mesmo eletrocardiógrafo EDAN SE-3. A rede pode aprender características do aparelho e do papel — a cor da grade, a fonte do cabeçalho — em vez de características do coração. Só um teste em ECGs de outro equipamento revelaria isso. |
| ECG Mendeley | **População do sul da Ásia** | Perfil étnico, prevalência de comorbidades e idade média diferem da população brasileira. |
| ECG Mendeley | **Vazamento pelo cabeçalho** | Se o cabeçalho não for recortado, a rede pode se apoiar em pistas espúrias (data do exame, ID sequencial) que se correlacionam com a classe apenas por causa da ordem de coleta — acurácia alta no papel, inútil na prática. |
| Textos | **Recorte editorial** | Artigos científicos revisados por pares descrevem a doença na linguagem técnica da academia, não na linguagem do paciente. Um assistente conversacional treinado só nisso responderá de forma incompreensível para quem pergunta. |

**Conclusão honesta:** nenhuma das três bases representa a população brasileira. Elas são adequadas para *aprender a construir* o CardioIA e para validar a arquitetura, mas um sistema destinado a uso clínico real no Brasil exigiria dados brasileiros e validação prospectiva local. Registrar isso aqui evita que a limitação seja esquecida quando os números de acurácia aparecerem na Fase 4.

---

## Estrutura do repositório

```
Fase_01/
├── README.md                      este documento
├── atividade.md                   enunciado da fase
├── dados/
│   └── cardioia_pacientes.csv     Parte 1 — 303 registros
├── assets/
│   ├── texto_01_...txt            Parte 2 — Estatística Cardiovascular Brasil 2023
│   └── texto_02_...txt            Parte 2 — Fatores de risco cardiovascular
├── imagens_ecg/                   Parte 3 — 128 ECGs em 4 pastas (fora do Git, ver nota)
└── scripts/
    ├── preparar_dados.py          baixa e prepara o CSV
    ├── extrair_textos.py          converte os PDFs em .txt
    └── baixar_imagens.py          baixa a amostra balanceada de ECGs
```

As 128 imagens ocupam 87 MB e **não são versionadas no Git** — elas vão para o Google Drive, como o enunciado pede, e o script as reconstrói a qualquer momento a partir da fonte original.

## Como reproduzir

```bash
pip install pandas pypdf

python Fase_01/scripts/preparar_dados.py    # -> dados/cardioia_pacientes.csv
python Fase_01/scripts/extrair_textos.py    # -> assets/*.txt
python Fase_01/scripts/baixar_imagens.py    # -> imagens_ecg/ (87 MB, alguns minutos)
```

Os três scripts baixam os dados direto da fonte oficial e não dependem de nenhum arquivo local nem de download manual. Rodar do zero em uma máquina limpa reproduz a entrega inteira.

---

## Referências

1. JANOSI, A.; STEINBRUNN, W.; PFISTERER, M.; DETRANO, R. **Heart Disease**. UCI Machine Learning Repository, 1988. DOI: [10.24432/C52P4X](https://doi.org/10.24432/C52P4X). Disponível em: https://archive.ics.uci.edu/dataset/45/heart+disease

2. OLIVEIRA, G. M. M. et al. **Estatística Cardiovascular – Brasil 2023**. *Arquivos Brasileiros de Cardiologia*, v. 121, n. 2, e20240079, 2024. DOI: [10.36660/abc.20240079](https://doi.org/10.36660/abc.20240079)

3. COLTRO, R. S. et al. **Frequência de fatores de risco cardiovascular em voluntários participantes de evento de educação em saúde**. *Revista da Associação Médica Brasileira*, v. 55, n. 5, p. 606-610, 2009. DOI: [10.1590/S0104-42302009000500028](https://doi.org/10.1590/S0104-42302009000500028)

4. KHAN, A. H. **ECG Images dataset of Cardiac Patients**. Mendeley Data, v. 2, 2021. DOI: [10.17632/gwbz3fsgp8.2](https://doi.org/10.17632/gwbz3fsgp8.2)

5. BRASIL. **Lei nº 13.709, de 14 de agosto de 2018** — Lei Geral de Proteção de Dados Pessoais (LGPD).

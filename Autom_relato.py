#!/usr/bin/env python
# coding: utf-8

# In[1]:


# =========================================================
# IMPORTANDO BIBLIOTECAS
# pip install selenium
# =========================================================

# Selenium -> automação/web scraping
from selenium import webdriver

# By -> ajuda encontrar elementos na tela
from selenium.webdriver.common.by import By

# datetime -> trabalhar com datas
from datetime import datetime

# time -> usar sleep
from time import sleep


# =========================================================
# ABRINDO NAVEGADOR
# =========================================================

driver = webdriver.Chrome()

# Maximiza a tela (opcional)
driver.maximize_window()


# =========================================================
# ACESSANDO O SITE
# =========================================================

driver.get("https://www.olx.com.br/estado-sp?q=smartphone")


# =========================================================
# ESPERANDO O SITE CARREGAR
# =========================================================

sleep(3)

# OBS:
# sleep NÃO é o ideal profissionalmente.
# Depois você aprende WebDriverWait.


# =========================================================
# PEGANDO TÍTULO
# =========================================================

# EXEMPLO:
# <h1 class="titulo">Relatório Financeiro</h1>

titulo = driver.find_element(
    By.CSS_SELECTOR,
    ".olx-adcard__title"
).text


# =========================================================
# PEGANDO DATA
# =========================================================

# EXEMPLO:
# <span class="data">28/05/2026</span>

data_site = driver.find_element(
    By.CSS_SELECTOR,
    ".olx-adcard__date"
).text


# =========================================================
# MOSTRANDO O QUE FOI CAPTURADO
# =========================================================

print("Título capturado:")
print(titulo)

print("\nData capturada:")
print(data_site)


# =========================================================
# CONVERTENDO TEXTO PARA DATA
# =========================================================

# transforma:
# "28/05/2026"
#
# em:
# datetime real

data_convertida = datetime.strptime(
    data_site,
    "%d/%m/%Y"
).date()


# =========================================================
# PEGANDO DATA DE HOJE
# =========================================================

hoje = datetime.today().date()


# =========================================================
# CALCULANDO DIFERENÇA
# =========================================================

diferenca = (hoje - data_convertida).days


# =========================================================
# VALIDANDO REGRA
# =========================================================

if diferenca <= 1:

    status = "OK"

else:

    status = f"(dados atualizados até {data_site})"


# =========================================================
# GERANDO CHECKLIST
# =========================================================

print("\n================ CHECKLIST ================\n")

if status == "OK":

    print(f"{titulo} - {data_site}")

else:

    print(f"{titulo} - {data_site} {status}")


# =========================================================
# FECHANDO NAVEGADOR
# =========================================================

driver.quit()


# In[4]:


pip install python-dotenv


# In[1]:


# =========================================================
# IMPORTANDO BIBLIOTECAS
#
# =========================================================

# Selenium -> automação/web scraping
from selenium import webdriver

# By -> localizar elementos
from selenium.webdriver.common.by import By

# datetime -> trabalhar com datas
from datetime import datetime, timedelta

# sleep -> pausas
from time import sleep


# =========================================================
# ABRINDO NAVEGADOR
# =========================================================

driver = webdriver.Chrome()

driver.maximize_window()


# =========================================================
# LISTAS DO CHECKLIST
# =========================================================

relatorios_ok = []

relatorios_erro = []


# =========================================================
# LISTA DE URLS
# =========================================================

urls = [

    "https://site1",

    "https://site2",

    "https://site3",

]


# =========================================================
# PERCORRENDO TODAS URLS
# =========================================================

for url in urls:


    # =====================================================
    # ACESSANDO SITE
    # =====================================================

    driver.get(url)


    # =====================================================
    # ESPERANDO SITE CARREGAR
    # =====================================================

    sleep(5)


    # =====================================================
    # PEGANDO TÍTULO
    # =====================================================

    titulo = driver.find_element(
        By.CSS_SELECTOR,
        ".olx-adcard__title"
    ).text


    # =====================================================
    # PEGANDO DATA
    # =====================================================

    data_site = driver.find_element(
        By.CSS_SELECTOR,
        ".olx-adcard__date"
    ).text


    # =====================================================
    # MOSTRANDO DADOS CAPTURADOS
    # =====================================================

    print("\n==================================================")
    print("             DADOS CAPTURADOS")
    print("==================================================\n")

    print(f"URL     : {url}")

    print(f"Título : {titulo}")

    print(f"Data   : {data_site}")


    # =====================================================
    # TRATANDO DATA
    # =====================================================

    # SE VIER "Hoje"
    if "Hoje" in data_site:

        data_convertida = datetime.today().date()


    # SE VIER "Ontem"
    elif "Ontem" in data_site:

        data_convertida = (
            datetime.today() - timedelta(days=1)
        ).date()


    # SE VIER DATA COMO:
    # "23 de mai, 17:28"
    else:


        # REMOVE HORÁRIO
        # "23 de mai, 17:28"
        #
        # vira:
        # "23 de mai"

        data_limpa = data_site.split(",")[0]


        # QUEBRA TEXTO
        # ["23", "de", "mai"]

        partes = data_limpa.split()


        # PEGA DIA
        dia = partes[0]


        # PEGA MÊS
        mes_texto = partes[2]


        # DICIONÁRIO DOS MESES
        meses = {

            "jan": "01",
            "fev": "02",
            "mar": "03",
            "abr": "04",
            "mai": "05",
            "jun": "06",
            "jul": "07",
            "ago": "08",
            "set": "09",
            "out": "10",
            "nov": "11",
            "dez": "12"

        }


        # CONVERTE MÊS
        mes = meses[mes_texto]


        # PEGA ANO ATUAL
        ano = datetime.today().year


        # MONTA DATA FINAL
        data_formatada = f"{dia}/{mes}/{ano}"


        # CONVERTE PARA DATA
        data_convertida = datetime.strptime(
            data_formatada,
            "%d/%m/%Y"
        ).date()


    # =====================================================
    # PEGANDO DATA DE HOJE
    # =====================================================

    hoje = datetime.today().date()


    # =====================================================
    # CALCULANDO DIFERENÇA
    # =====================================================

    diferenca = (hoje - data_convertida).days


    # =====================================================
    # VALIDANDO RELATÓRIO
    # =====================================================

    # SE ESTIVER ATUALIZADO
    if diferenca <= 1:

        relatorios_ok.append(titulo)


    # SE ESTIVER DESATUALIZADO
    else:

        relatorios_erro.append(
            f"{titulo} → dados atualizados até {data_site}"
        )


# =========================================================
# EXIBINDO CHECKLIST FINAL
# =========================================================

print("\n")
print("╔══════════════════════════════════════════════╗")
print("║         CHECKLIST DE RELATÓRIOS             ║")
print("╚══════════════════════════════════════════════╝")


# =========================================================
# RELATÓRIOS ATUALIZADOS
# =========================================================

print("\n✅ RELATÓRIOS ATUALIZADOS:\n")


# VERIFICA SE EXISTE ITEM NA LISTA
if len(relatorios_ok) > 0:


    # PERCORRE TODOS ITENS
    for relatorio in relatorios_ok:


        # MOSTRA ITEM
        print(f"   • {relatorio}")


# CASO NÃO TENHA RELATÓRIOS OK
else:

    print("   Nenhum relatório atualizado")


# =========================================================
# RELATÓRIOS COM ERRO
# =========================================================

print("\n❌ RELATÓRIOS COM ERRO DE ATUALIZAÇÃO:\n")


# VERIFICA SE EXISTE ITEM NA LISTA
if len(relatorios_erro) > 0:


    # PERCORRE TODOS ITENS
    for relatorio in relatorios_erro:


        # MOSTRA ITEM
        print(f"   • {relatorio}")


# CASO NÃO TENHA ERROS
else:

    print("   Nenhum relatório com erro")


print("\n════════════════ FIM DO RELATÓRIO ════════════════\n")


# =========================================================
# FECHANDO NAVEGADOR
# =========================================================

driver.quit()


#Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import math

#Iniciando o cronometro do programa
tempo_zero = time.time()
#Acessando o site:
navegador = webdriver.Chrome()
navegador.get('https://orteil.dashnet.org/cookieclicker/')
navegador.maximize_window()

#Configuracoes Iniciais
    #Idioma
        #Tentando clicar no botão de portugues ate conseguir
while True:
    try:
        botao_portugues = navegador.find_element(By.XPATH, '//*[@id="langSelect-PT-BR"]')
        botao_portugues.click()
        break
    except:
        pass
    #Nome da padaria
        #Tentando clicar no botão de nomear padaria ate conseguir
while True:
    try:
        botao_nome_padaria = navegador.find_element(By.XPATH, '//*[@id="bakeryName"]')
        botao_nome_padaria.click()
        break
    except:
        pass
        #Nomeando a padaria
caixa_nome_padaria = navegador.find_element(By.XPATH, '//*[@id="bakeryNameInput"]')
caixa_nome_padaria.send_keys('ITA Jr - Guabiru' + Keys.ENTER)
        #Menu de estatisticas
botao_estatistica = navegador.find_element(By.XPATH, '//*[@id="statsButton"]')
botao_estatistica.click()
        #Melhorando a vizualizacao
navegador.execute_script("document.body.style.zoom='75%'")
#Iniciando o cronometro do jogo
tempo_inicial = time.time()
#Scraping
    #Dados a serem coletados
cookies = 0
cps = 0
melhorias = []
    #Dados Iniciais
quantidade = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cps_construcao = [0.1, 1, 8, 47, 260, 1400, 7800, 44000, 260000, 1600000, 10000000, 65000000, 430000000, 2900000000, 21000000000, 150000000000, 1100000000000, 8300000000000, 64000000000000, 510000000000000]
preco_construcao = [15, 100, 1100, 12000, 120000, 1400000, 20000000, 330000000, 5100000000, 75000000000, 1000000000000, 14000000000000, 170000000000000, 2100000000000000, 26000000000000000, 310000000000000000, 3800000000000000000, 46000000000000000000, 550000000000000000000, 64000000000000000000000]
n_melhorias = 0
cps_selenium = 13
multiplo_de_clicks = 1
cronometro = 0
preco_melhoria = []
const_melhoria = []
catalogo_melhorias_id = [
    [0, 1, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [7, 8, 9, 44, 110, 192, 294, 307, 428, 480, 506, 662, 700, 743, 840],
    [10, 11, 12, 45, 111, 193, 295, 308, 429, 481, 507, 663, 701, 744, 841],
    [16, 17, 18, 47, 113, 195, 296, 309, 430, 482, 508, 664, 702, 745, 824],
    [13, 14, 15, 46, 112, 194, 297, 310, 431, 483, 509, 665, 703, 746, 843],
    [232, 233, 234, 235, 236, 237, 298, 311, 432, 484, 510, 666, 704, 747, 844],
    [238, 239, 240, 241, 242, 243, 299, 312, 433, 485, 511, 667, 705, 748, 845],
    [244, 245, 246, 247, 248, 249, 300, 313, 434, 486, 512, 668, 706, 749, 846],
    [19, 20, 21, 48, 114, 196, 301, 314, 435, 487, 513, 669, 707, 750, 847],
    [22, 23, 24, 49, 115, 197, 302, 315, 436, 488, 514, 670, 708, 751, 848],
    [25, 26, 27, 50, 116, 198, 303, 316, 437, 489, 515, 671, 709, 752, 849],
    [28, 29, 30, 51, 117, 199, 304, 317, 438, 490, 516, 672, 710, 753, 850],
    [99, 100, 101, 102, 118, 200, 305, 318, 439, 491, 517, 673, 711, 754, 851],
    [175, 176, 177, 178, 179, 201, 306, 319, 440, 492, 518, 674, 712, 755, 852],
    [416, 417, 418, 419, 420, 421, 422, 423, 441, 493, 519, 675, 713, 756, 853],
    [522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 676, 714, 757, 854],
    [594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 677, 715, 758, 855],
    [685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 716, 759, 856, 856],
    [730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 760, 857],
    [826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 858]
]
catalogo_melhorias_preco_multiplicador = [10, 50, 500, 50000, 5000000, 500000000, 500000000000, 500000000000000, 500000000000000000, 500000000000000000000, 5000000000000000000000000, 50000000000000000000000000000, 500000000000000000000000000000000, 5000000000000000000000000000000000000, 50000000000000000000000000000000000000000]

#Coleta
def raspar():
    global cookies, cps, preco_construcao, tempo_inicial, cronometro, melhorias, catalogo_melhorias_preco_multiplicador, preco_melhoria, const_melhoria
        #Cronometro
    cronometro = time.time() - tempo_inicial
        #Setando dados
    preco_inicial = [15, 100, 1100, 12000, 120000, 1400000, 20000000, 330000000, 5100000000, 75000000000, 1000000000000, 14000000000000, 170000000000000, 2100000000000000, 26000000000000000, 310000000000000000, 3800000000000000000, 46000000000000000000, 550000000000000000000, 64000000000000000000000]
        #Cookies e CPS
    informacao = navegador.find_element(By.XPATH, "//div[@id = 'cookies']").text
    #Processamento
    dados = informacao.split('\n',-1)
    if len(dados) == 3:
        dados[0] = dados[0] + ' ' + dados[1]
        dados.pop(1)
        #Apagando as palavras
    for i in range(len(dados)):
        dados[i] = dados[i].replace(' cookies','')
        dados[i] = dados[i].replace(' cookie', '')
        dados[i]= dados[i].replace('por segundo: ','')
        dados[i]= dados[i].replace(',','')
        #Traduzindo os multiplicadores
    multiplicadores = {
        'million': 10 ** 6,
        'billion': 10 ** 9,
        'trillion': 10 ** 12,
        'quadrillion': 10 ** 15,
        'quintillion': 10 ** 18,
        'sextillion': 10 ** 21,
        'septillion': 10 ** 24,
        'octillion': 10 ** 27,
        'nonillion': 10 ** 30,
        'decillion': 10 ** 33,
        'undecillion': 10 ** 36,
        'duodecillion': 10 ** 39,
        'tredecillion': 10 ** 42,
        'quattuordecillion': 10 ** 45,
        'quindecillion': 10 ** 48,
        'sexdecillion': 10 ** 51,
        'septendecillion': 10 ** 54,
        'octodecillion': 10 ** 57,
        'novemdecillion': 10 ** 60,
        'vigintillion': 10 ** 63,
        'unvigintillion': 10 ** 66,
        'duovigintillion': 10 ** 69,
    }
    def converter_lista_com_sufixos(lista):
        for i in range(len(lista)):
            for sufixo, fator in multiplicadores.items():
                if sufixo in lista[i]:
                    lista[i] = lista[i].replace(f' {sufixo}', '')
                    lista[i] = float(lista[i]) * fator
                    break
    converter_lista_com_sufixos(dados)
    #Aplicando os valores
    cookies = int(dados[0])
    cps = float(dados[-1])
    #Preco por construcao
    for i in range(len(quantidade)):
        preco_construcao[i] = (math.ceil(preco_inicial[i] * 1.15 ** quantidade[i]))
    # Escaneando as melhorias disponíveis
    ids_melhorias = []
    preco_melhoria.clear()
    const_melhoria.clear()
    try:
        melhorias = navegador.find_elements(By.XPATH, "//div[@id = 'upgrades']/div")
        for melhoria in melhorias:
            ids_melhorias.append(melhoria.get_attribute('data-id'))
        #Caracteristicas melhorias
        for id_ in ids_melhorias:
            id_ = int(id_)
            verificador = 0
            for construcao in catalogo_melhorias_id:
                if id_ in construcao:
                    verificador = 1
                    const = catalogo_melhorias_id.index(construcao)
                    nivel = construcao.index(id_)
                    const_melhoria.append(const)
                    if id_ == 0:
                        preco_melhoria.append(100)
                    elif id_ == 1:
                        preco_melhoria.append(500)
                    elif id_ == 2:
                        preco_melhoria.append(10000)
                    else:
                        preco = preco_inicial[const] * catalogo_melhorias_preco_multiplicador[nivel]
                        preco_melhoria.append(preco)
            if verificador == 0:
                preco_melhoria.append(-1)
                const_melhoria.append(-1)
    except:
        pass
    #Apresentando valores
    print("Cookies: ", cookies)
    print("CPS: ", cps)
    print("Preco_c: \n", preco_construcao)
    print("Quantidade_c: \n", quantidade)
    print("CPS_c: \n", cps_construcao)
    print("Const_Melhoria: \n", const_melhoria)
    print("Preco_m: \n",preco_melhoria)
    print("Multiplo de clicks: ", multiplo_de_clicks)
    print("Tempo: ", cronometro)
    print("CPS sellenium: ", cps_selenium)
    print("\n")

#Acoes
   #Clicar no cookie
botao_cookie = navegador.find_element(By.XPATH, '//*[@id="bigCookie"]')
def cookie(vezes):
    for i in range(vezes):
        botao_cookie.click()
    #Comprar construcao
def comprar(numero_do_id):
    print(f"{cookies}>={preco_construcao[numero_do_id]}?")
    if cookies >= preco_construcao[numero_do_id]:
        navegador.execute_script("document.body.style.zoom='25%'") #Deixar todas as construcoes na tela visível
        botao_product = navegador.find_element(By.XPATH, f"//div[@id = 'store']/div[@id = 'products']/div[@id = 'product{numero_do_id}']")
        botao_product.click()
        quantidade[numero_do_id] += 1
        navegador.execute_script("document.body.style.zoom='75%'")
        print("Compra valida\n")
    else:
        print("Compra Invalida\n")
    #Comprar Melhoria
def comprar_melhoria(melhoria):
    global n_melhorias, cps_construcao, multiplo_de_clicks
    try:
        print(f"{cookies}>={preco_melhoria[melhoria]}?")
        if cookies >= preco_melhoria[melhoria]:
            print("Compra valida\n")
            while True:
                try:
                    melhoria_button = navegador.find_element(By.XPATH, f'//*[@id="upgrade{melhoria}"]')
                    if melhoria <= 4:
                        melhoria_button.click()
                    else:
                        ActionChains(navegador) \
                            .move_to_element(navegador.find_element(By.XPATH,"//div[@id = 'store']/div[@id = 'products']/div[@id = 'product0']")) \
                            .perform()
                        melhoria_button.click()
                    n_melhorias = n_melhorias + 1
                    cps_construcao[const_melhoria[melhoria]] *= 2
                    if const_melhoria[melhoria] == 0:
                        multiplo_de_clicks *= 2
                    break
                except:
                    cookie(8)
        else:
            print("Compra invalida\n")
    except:
        pass

#Decisao
    #Parametros usados para tomar uma decisao.
pontuacao_c = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
pontuacao_m = []
escolha_m = "nulo"
escolha_c = "nulo"
    #Tempo definido para o programa executar o jogo com a melhor performace
tempo_de_operacao = 60 * 5
    #Tempo de inicializacao
tempo_de_inicializacao = tempo_inicial - tempo_zero
    #Tempo de jogo apos o desconto do tempo de inicializacao
tempo_de_jogo = tempo_de_operacao - tempo_de_inicializacao
    #Heuristica
tipo = 'nulo'
def heuristica():
    global tempo_de_jogo, cookies, cps, preco_construcao, cps_construcao, cps_selenium, pontuacao_c, preco_melhoria, pontuacao_m, tipo, escolha_c, escolha_m
    #Pontuação Construcoes
    for i in range(20):
        if cookies>=preco_construcao[i]:
            pontuacao_c[i] = (cps_construcao[i]) * (tempo_de_jogo - cronometro) / preco_construcao[i] #Quantos cookies cada cookie gasto ira gerar
        else:
            tempo_de_espera = (preco_construcao[i] - cookies) / (cps + cps_selenium * multiplo_de_clicks)
            pontuacao_c[i] = (cps_construcao[i]) * (tempo_de_jogo - cronometro - tempo_de_espera)/preco_construcao[i] #Idem
    escolha_c = pontuacao_c.index(max(pontuacao_c))
    print("Max C: ", max(pontuacao_c))
    #Pontuacao Melhorias:
    pontuacao_m.clear() #Potuacao calculada analogamente as construcoes
    try:
        for i in range(len(melhorias)):
            if const_melhoria[i] == -1:
                pontuacao_m.append(-1)
            elif const_melhoria[i] == 0:
                if cookies >= preco_melhoria[i]:
                    pontuacao_m.append((cps_construcao[i] * quantidade[i] + cps_selenium * multiplo_de_clicks) * (tempo_de_jogo - cronometro) / preco_melhoria[i])
                else:
                    tempo_de_espera = (preco_melhoria[i] - cookies) / (cps + cps_selenium * multiplo_de_clicks)
                    pontuacao_m.append((cps_construcao[i] * quantidade[i] + cps_selenium * multiplo_de_clicks) * (tempo_de_jogo - cronometro - tempo_de_espera) / preco_melhoria[i])
            else:
                if cookies >= preco_melhoria[i]:
                    pontuacao_m.append((cps_construcao[i]) * quantidade[i] * (tempo_de_jogo - cronometro) / preco_melhoria[i])
                else:
                    tempo_de_espera = (preco_melhoria[i] - cookies) / (cps + cps_selenium * multiplo_de_clicks)
                    pontuacao_m.append((cps_construcao[i]) * quantidade[i] * (tempo_de_jogo - cronometro - tempo_de_espera) / preco_melhoria[i])
        if not pontuacao_m:
            pass
        else:
            escolha_m = pontuacao_m.index(max(pontuacao_m))
            print("Max M: ", max(pontuacao_m))
    except:
        pass
    #Contrucão x Melhoria:
    if not pontuacao_m:
        escolha_final = escolha_c
        tipo = 'construcao'
    else:
        if pontuacao_m[escolha_m] >= pontuacao_c[escolha_c]:
            escolha_final = escolha_m
            tipo = 'melhoria'
        else:
            escolha_final = escolha_c
            tipo = 'construcao'
    print(escolha_final)
    print(tipo)
    print("\n")
    return escolha_final

#Execucao
def decisao_e_execucao(metodo_de_escolha):
    global cps_selenium
    decisao = int(f"{metodo_de_escolha}")
    if tipo == 'construcao':
        if pontuacao_c[decisao] <= 0:
            tempo_finalizacao = tempo_de_jogo - cronometro
            clicks_finalizacao = math.ceil((cps + cps_selenium * multiplo_de_clicks) * tempo_finalizacao / multiplo_de_clicks)
            cookie(clicks_finalizacao)
        else:
            if cookies>=preco_construcao[decisao]:
                comprar(decisao)
                cookie(4)
            else:
                tempo_de_espera = (preco_construcao[decisao] - cookies) / (cps + cps_selenium * multiplo_de_clicks)
                cookies_clicados_na_espera = math.ceil(((preco_construcao[decisao] - cookies) - cps * tempo_de_espera)/multiplo_de_clicks)
                t_i = time.time()
                cookie(cookies_clicados_na_espera)
                t_f = time.time()
                if cookies_clicados_na_espera > 75:
                    cps_selenium = cookies_clicados_na_espera / (t_f - t_i)
                raspar()
                comprar(decisao)
                cookie(4)
    elif tipo == 'melhoria':
        if pontuacao_m[decisao] <= 0:
            tempo_finalizacao = tempo_de_jogo - cronometro
            clicks_finalizacao = math.ceil((cps + cps_selenium * multiplo_de_clicks) * tempo_finalizacao / multiplo_de_clicks)
            cookie(clicks_finalizacao)
        else:
            if cookies>=preco_melhoria[decisao]:
                comprar_melhoria(decisao)
                cookie(4)
            else:
                tempo_de_espera = (preco_melhoria[decisao] - cookies) / (cps + cps_selenium * multiplo_de_clicks)
                cookies_clicados_na_espera = int(math.ceil(((preco_melhoria[decisao] - cookies) - cps * tempo_de_espera) / multiplo_de_clicks))
                t_i = time.time()
                cookie(cookies_clicados_na_espera)
                t_f = time.time()
                if cookies_clicados_na_espera > 75:
                    cps_selenium = cookies_clicados_na_espera / (t_f - t_i)
                raspar()
                comprar_melhoria(decisao)
                cookie(4)

############################################################################
# Bloco de comandos
############################################################################
    #Setando o tempo em que o bot maximizara o numero de cookies assados
tempo_de_operacao = 5 * 60
tempo_de_jogo = tempo_de_operacao - tempo_de_inicializacao
    #Setando o CPS Selenium inicial
cps_selenium = 17.50 #Isso é so um chute com base na media de clicks por segundo que meu computador alcanca com esse programa
                     #Ao longo jogo o programa calculará recorrentemente o cps_selenium com base nos dados coletados, garantindo uma boa precisao
    #Comprando um mouse, pois é barato e desbloqueia 2 melhorias, que antes o 'raspar()' nao identificava, assim, permitindo que o bot tenha mais informacoes no inicio do jogo
cookie(18) #Um pouco a mais que 15 pois o site demora alguns segundos para carregar as informacoes, provavelmente sera lido cookies = 17, assim 18 é um valor seguranca
raspar()
comprar(0)
    #Daqui em diante o programa vai raspar o site, tomar as proprias decisoes e executa-las ate acabar o tempo previsto
while cronometro < tempo_de_jogo:
    raspar()
    decisao_e_execucao(heuristica())
    print(tempo_de_jogo)
    #Agora o objetivo do bot é apenas zerar o jogo, sem estar previsto um tempo fixo
tempo_de_operacao = 60 * 60 * 24 * 365 #Grande em comparacao a qualquer 'tempo_de_espera'
tempo_de_jogo = tempo_de_operacao - tempo_de_inicializacao
        #Modo Evolucao
while cps < 10 ** 28: #Ordem de grandeza das construcoes mais caras
    raspar()
    decisao_e_execucao(heuristica())
        #Comprando construcoes:
for i in range(20):
    while quantidade[i] < 1000: #Sao necessarias 1000 unidades de cada construcao para ter acesso a todas as melhorias
        raspar()
        try:
            comprar(i)
        finally:
            cookie(16*30) #+- 30s
        #Comprando melhorias:
while n_melhorias < 716:
    raspar()
    try:
        comprar_melhoria(0) #melhoria mais barata disponivel
    finally:
        cookie(16*30)
#Fim
print("Tempo total: \n", cronometro)
print("Cookie Clicker Finalizado")

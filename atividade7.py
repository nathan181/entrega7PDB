#aula 08/06
from collections import Counter
from matplotlib import pyplot as plt
import random
import math

def quantidade_de_usuarios_na_rede():
    return 100

def gera_amizades(numero_conexoes_desejado, qtde_usuarios_na_rede): #gerar lista de tuplas com amigos
    conexoes = []
    for i in range(numero_conexoes_desejado):
        while True:
            u1 = random.randint(0, qtde_usuarios_na_rede - 1)
            u2 = random.randint(0, qtde_usuarios_na_rede - 1)
            if u1 != u2:
                conexoes.append((u1, u2))
                break
    return [aux for aux in set(conexoes)]

def quantidade_de_amigos(amizades):
    a = Counter(i for i, _ in amizades)
    b = Counter(i for _, i in amizades)
    tudo = a + b
    return Counter(x for x in tudo.values())



def gera_histograma_contagem_amigos(quantidade_de_amigos, qtde_usuarios_na_rede):
    
    xs = range(qtde_usuarios_na_rede)
    ys = [quantidade_de_amigos[x] for x in xs]
    
    plt.bar(xs, ys)
    plt.axis ([0, qtde_usuarios_na_rede, 0, qtde_usuarios_na_rede/4])
    plt.title("Histograma da contagem de amigos")
    plt.xlabel('# de amigos')
    plt.ylabel('# de pessoas')

    plt.show()


def media_qtde_amigos(qtde_amigos):
    so_qtdes = [x*y for x, y in qtde_amigos.items()]
    return sum (so_qtdes) / sum(x for x in qtde_amigos.values())


def teste_gera_histograma_contagem_amigos():
    qtde_usuarios_na_rede = quantidade_de_usuarios_na_rede()
    amizades = gera_amizades(1000, qtde_usuarios_na_rede)
    qtde_amigos = quantidade_de_amigos(amizades)
    gera_histograma_contagem_amigos(qtde_amigos, qtde_usuarios_na_rede)

def teste_media_qtde_amigos():
    print(f'Média: {media_qtde_amigos(quantidade_de_amigos(gera_amizades(5000, quantidade_de_usuarios_na_rede())))}')


def mediana_qtde_amigos (qtde_amigos):
    so_qtde = [x*y for x, y in qtde_amigos.items()]
    ordenada = sorted(so_qtde)
    meio = len(ordenada) // 2
    return ordenada[meio] if meio % 2 == 1 else (ordenada[meio - 1] + ordenada[meio]) / 2

def teste_mediana_qtde_amigos():
        print(
            f'Mediana: {mediana_qtde_amigos(quantidade_de_amigos(gera_amizades(5000, quantidade_de_usuarios_na_rede())))}'
            )

def quantil (qtde_amigos, percentual):
    so_qtdes = [x * y for x, y in qtde_amigos.items()]
    indice = int (percentual * len(so_qtdes))
    return sorted(so_qtdes)[indice]

def teste_quantil():
    print(
    f'Quantil(10%): {quantil(quantidade_de_amigos(gera_amizades(50, quantidade_de_usuarios_na_rede())), 0.1)}'
    )

def moda_qtde_amigos (qtde_amigos):
    moda = max(qtde_amigos.values())
    return [x for x, count in qtde_amigos.items() if count == moda]

def teste_moda_qtde_amigos():
    print(
    f'Moda(s): {moda_qtde_amigos(quantidade_de_amigos(gera_amizades(5000, quantidade_de_usuarios_na_rede())))}'
    )

def amplitude_dos_dados (qtde_amigos):
    so_qtdes = [x * y for x, y in qtde_amigos.items()]
    return max(so_qtdes) - min(so_qtdes)


def teste_amplitude_dos_dados():
    print(
    f'Amplitude: {amplitude_dos_dados(quantidade_de_amigos(gera_amizades(5000, quantidade_de_usuarios_na_rede())))}'
    )    

def teste_variancia():
    print(
    f'Variancia: {variancia(quantidade_de_amigos(gera_amizades(5000, quantidade_de_usuarios_na_rede())))}'
    ) 

def teste_desvio_padrao():
    print(
    f'Desvio Padrao: {desvio_padrao(quantidade_de_amigos(gera_amizades(5000, quantidade_de_usuarios_na_rede())))}'
    ) 


def diferencas_em_relacao_a_media (qtde_amigos):
    so_qtdes = [x * y for x, y in qtde_amigos.items()]
    media = media_qtde_amigos (qtde_amigos)
    return [x - media for x in so_qtdes]

def soma_dos_quadrados (diferencas):
    return sum (x**2 for x in diferencas)

def variancia (qtde_amigos):
    so_qtdes = [x * y for x, y in qtde_amigos.items()]
    return soma_dos_quadrados(diferencas_em_relacao_a_media(qtde_amigos)) / (len(so_qtdes) - 1)

def desvio_padrao (qtde_amigos):
    return math.sqrt(variancia(qtde_amigos))





#----------------------------------Atividade Semana 07-----------------------------------------
# 1 Escreva uma função que constrói um histograma que mostra a quantidade de amigos que pessoas de cada sexo têm.

def gera_histograma_contagem_amigos_por_sexo(quantidade_de_amigos, qtde_usuarios_na_rede):
    homens = qtde_usuarios_na_rede - random.randint(0, qtde_usuarios_na_rede)
    hs = range(homens)
    zs = [quantidade_de_amigos[x] for x in hs]
    
    plt.bar(hs, zs)
    plt.axis ([0, homens, 0, homens])
    plt.title("Histograma da contagem de amigos dos homens")
    plt.xlabel('# de amigos')
    plt.ylabel('# de homens')
    plt.show()

    mulheres = qtde_usuarios_na_rede - homens
    fs = range(mulheres)
    ys = [quantidade_de_amigos[x] for x in fs]
    plt.bar(fs, ys)
    plt.axis ([0, mulheres, 0, mulheres])
    plt.title("Histograma da contagem de amigos das mulheres")
    plt.xlabel('# de amigos')
    plt.ylabel('# de mullheres')
    plt.show()


#-----------------------------------------------------------------------------------------
# 2 Escreva uma função que constrói um histograma que mostra a quantidade de amigos que pessoas de cada idade têm.

def gera_histograma_contagem_amigos_por_idade(quantidade_de_amigos, qtde_usuarios_na_rede):
    
    lista_idades = []
    for item in range(qtde_usuarios_na_rede):
        lista_idades.append(random.randint(13, 100))


    xs = range(qtde_usuarios_na_rede)
    ys = [quantidade_de_amigos[x] for x in lista_idades]
    
    plt.bar(xs, ys)
    plt.axis ([0, qtde_usuarios_na_rede, 0, qtde_usuarios_na_rede/4])
    plt.title("Histograma da contagem de amigos")
    plt.xlabel('# de amigos')
    plt.ylabel('# de pessoas')
    plt.show()

#----------------------------------------------------------------------------------------------------
# 3 Escreva uma função que calcula a variância e o desvio padrão da idade das pessoas do sexo
# masculino que tenham pelo menos 22 anos.

def variancia_e_desvio_padrao():
    qtde_usuarios = quantidade_de_usuarios_na_rede()
    qtde_homens = qtde_usuarios - random.randint(0, qtde_usuarios)
    
    lista_idades = []
    maior_21 = []
    for item in range(qtde_homens):
        lista_idades.append(random.randint(13, 100))

    for item in lista_idades:
        if item > 21:
            maior_21.append(item)
    
    media_idade = sum (maior_21) / len(maior_21)

    diferencas_em_relacao_a_media = [x - media_idade for x in maior_21]

    soma_dos_quadrados = sum(x**2 for x in diferencas_em_relacao_a_media)

    variancia = soma_dos_quadrados / (len(maior_21) - 1)

    desvio_padrao = math.sqrt(variancia)

    print('Quantidade de usuarios na rede: ', qtde_usuarios)
    print('Quantidade de homens na rede: ', qtde_homens)
    print('Idade dos homens:', lista_idades)
    print('Maiores de 21: ', maior_21)
    print('Media das idades: ', media_idade)
    print('Diferenças em relação a media: ', diferencas_em_relacao_a_media)
    print('Soma dos quadrados: ', soma_dos_quadrados)
    print('Variancia: ', variancia)
    print('Desvio Padrao: ', desvio_padrao)
    

    pass




def main():
    
    # teste_gera_histograma_contagem_amigos()
    # teste_media_qtde_amigos()
    # teste_mediana_qtde_amigos()
    # teste_quantil()
    # teste_moda_qtde_amigos()
    # teste_amplitude_dos_dados()
    # teste_variancia()
    # teste_desvio_padrao
    variancia_e_desvio_padrao()
    pass

main()
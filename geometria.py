# LIVRO = Steinbruch
# LIBS INDISPENSÁVEIS:
import math  # [arcos]

# CAPITULO 1: (VETORES)

def achar_versor(vetor):
    """
    Calcula o versor (vetor unitário) de um vetor dado.
    
    Entrada:
    - vetor: lista de números representando um vetor.
    
    Saída:
    - vetor_final: lista de números representando o versor do vetor dado.
    """
    vetor_final = []
    modulo = modulo_vetor(vetor)
    for componente in vetor:
        vetor_final.append(componente / modulo)
    return vetor_final


# CAPITULO 2: (VETORES)

def vetores_iguais(vetor1, vetor2):
    """
    Verifica se dois vetores são iguais.
    
    Entradas:
    - vetor1: lista de números representando o primeiro vetor.
    - vetor2: lista de números representando o segundo vetor.
    
    Saída:
    - Booleano indicando se os vetores são iguais (True) ou não (False).
    """
    auxiliar = 0
    for i in range(len(vetor1)):
        if vetor1[i] != vetor2[i]:
            auxiliar = 1
    return auxiliar == 0


def soma_vetores(vetor1, vetor2):
    """
    Calcula a soma de dois vetores.
    
    Entradas:
    - vetor1: lista de números representando o primeiro vetor.
    - vetor2: lista de números representando o segundo vetor.
    
    Saída:
    - vetor_final: lista de números representando a soma dos dois vetores.
    """
    vetor_final = []
    for i in range(len(vetor1)):
        vetor_final.append(vetor1[i] + vetor2[i])
    return vetor_final


def diferenca_vetores(vetor1, vetor2):
    """
    Calcula a diferença entre dois vetores.
    
    Entradas:
    - vetor1: lista de números representando o primeiro vetor.
    - vetor2: lista de números representando o segundo vetor.
    
    Saída:
    - vetor_final: lista de números representando a diferença entre os dois vetores.
    """
    vetor_final = []
    for i in range(len(vetor1)):
        vetor_final.append(vetor1[i] - vetor2[i])
    return vetor_final


def escalando_um_vetor(vetor, escalar):
    """
    Escala um vetor por um fator escalar.
    
    Entrada:
    - vetor: lista de números representando o vetor.
    - escalar: número pelo qual o vetor será escalado.
    
    Saída:
    - vetor_final: lista de números representando o vetor escalado.
    """
    vetor_final = []
    for componente in vetor:
        vetor_final.append(componente * escalar)
    return vetor_final


def sao_colineares_angulo(vetor1, vetor2):
    """
    Verifica se dois vetores são colineares usando o ângulo entre eles.
    
    Entradas:
    - vetor1: lista de números representando o primeiro vetor.
    - vetor2: lista de números representando o segundo vetor.
    
    Saída:
    - Booleano indicando se os vetores são colineares (True) ou não (False).
    """
    _, angulo = angulo_entre_vetores(vetor1, vetor2)
    return angulo == 0 or angulo == 180


def sao_colineares_razao(vetor1, vetor2):
    """
    Verifica se dois vetores são colineares usando a razão entre seus componentes.
    
    Entradas:
    - vetor1: lista de números representando o primeiro vetor.
    - vetor2: lista de números representando o segundo vetor.
    
    Saída:
    - Booleano indicando se os vetores são colineares (True) ou não (False).
    """
    razao = vetor1[0] / vetor2[0]
    for i in range(len(vetor1)):
        if vetor1[i] / vetor2[i] != razao:
            return False
    return True


# CAPÍTULO 3: (PRODUTO VETORES)

def produto_escalar(vetor1, vetor2):
    """
    Calcula o produto escalar entre dois vetores.
    
    Entradas:
    - vetor1: lista de números representando o primeiro vetor.
    - vetor2: lista de números representando o segundo vetor.
    
    Saída:
    - resultado: número representando o produto escalar dos dois vetores.
    """
    resultado = 0
    for i in range(len(vetor1)):
        resultado += vetor1[i] * vetor2[i]
    return resultado


def sao_ortogonais(vetor1, vetor2):
    """
    Verifica se dois vetores são ortogonais.
    
    Entradas:
    - vetor1: lista de números representando o primeiro vetor.
    - vetor2: lista de números representando o segundo vetor.
    
    Saída:
    - Booleano indicando se os vetores são ortogonais (True) ou não (False).
    """
    resultado = produto_escalar(vetor1, vetor2)
    return resultado == 0


def modulo_vetor(vetor):
    """
    Calcula o módulo (magnitude) de um vetor.
    
    Entrada:
    - vetor: lista de números representando o vetor.
    
    Saída:
    - Número representando o módulo do vetor.
    """
    soma_potencias = 0
    for componente in vetor:
        soma_potencias += componente**2
    return soma_potencias**(0.5)


def angulo_entre_vetores(vetor1, vetor2):
    """
    Calcula o ângulo entre dois vetores em radianos e graus.
    
    Entradas:
    - vetor1: lista de números representando o primeiro vetor.
    - vetor2: lista de números representando o segundo vetor.
    
    Saída:
    - angulo_rad: ângulo entre os vetores em radianos.
    - angulo_graus: ângulo entre os vetores em graus.
    """
    modulo1 = modulo_vetor(vetor1)
    modulo2 = modulo_vetor(vetor2)
    escalar_prod = produto_escalar(vetor1, vetor2)
    modulos_prod = round((modulo1 * modulo2),5)
    angulo_rad = math.acos(escalar_prod / modulos_prod)
    angulo_graus = math.degrees(angulo_rad)
    return angulo_rad, angulo_graus

def vetor_projetado(vetor1, vetor2):
    """
    Calcula a projeção de um vetor sobre outro vetor.
    
    Entradas:
    - vetor1: lista de números representando o primeiro vetor.
    - vetor2: lista de números representando o segundo vetor.
    
    Saída:
    - vetor_proj: lista de números representando a projeção do vetor1 sobre o vetor2.
    """
    prod_esc1 = produto_escalar(vetor1, vetor2)
    prod_esc2 = produto_escalar(vetor2, vetor2)
    razao = prod_esc1 / prod_esc2
    vetor_proj = escalando_um_vetor(vetor2, razao)
    return vetor_proj


def prod_vetorial(vetor1, vetor2):
    """
    Calcula o produto vetorial entre dois vetores em 3D.
    
    Entradas:
    - vetor1: lista de 3 números representando o primeiro vetor.
    - vetor2: lista de 3 números representando o segundo vetor.
    
    Saída:
    - vetor_resultado: lista de 3 números representando o produto vetorial.
    
    Levanta:
    - ValueError: Se os vetores não têm a mesma dimensionalidade ou não são 3D.
    """
    if len(vetor1) != len(vetor2) or len(vetor1) != 3:
        raise ValueError("Os vetores devem ter a mesma dimensionalidade!")

    x = vetor1[1] * vetor2[2] - vetor1[2] * vetor2[1]
    y = vetor1[2] * vetor2[0] - vetor1[0] * vetor2[2]
    z = vetor1[0] * vetor2[1] - vetor1[1] * vetor2[0]

    vetor_resultado = [x, y, z]

    return vetor_resultado


def prod_misto(vetor1, vetor2, vetor3):
    """
    Calcula o produto misto entre três vetores.
    
    Entradas:
    - vetor1: lista de 3 números representando o primeiro vetor.
    - vetor2: lista de 3 números representando o segundo vetor.
    - vetor3: lista de 3 números representando o terceiro vetor.
    
    Saída:
    - Número representando o produto misto dos três vetores.
    """
    prod_vet = prod_vetorial(vetor2, vetor3)
    prod_esc = produto_escalar(vetor1, prod_vet)
    return prod_esc

# CAPITULO 4: (A RETA)

def equ_vetorial_reta(pontoA, pontoB, vetor):
    """
    Retorna a equação vetorial de uma reta passando por um ponto e seguindo uma direção.
    
    Entradas:
    - pontoA: lista de números representando o ponto inicial da reta.
    - pontoB: lista de números representando um segundo ponto da reta.
    - vetor: lista de números representando o vetor diretor da reta (opcional).
    
    Saída:
    - String representando a equação vetorial da reta.
    """
    if vetor is None:
        vetor = diferenca_vetores(pontoB, pontoA)
    reta = f"Reta = {pontoA} + t*{vetor}"
    return reta
    

def equ_parametrica_reta(pontoA, pontoB, vetor):
    """
    Retorna a equação paramétrica de uma reta passando por um ponto e seguindo uma direção.
    
    Entradas:
    - pontoA: lista de números representando o ponto inicial da reta.
    - pontoB: lista de números representando um segundo ponto da reta.
    - vetor: lista de números representando o vetor diretor da reta (opcional).
    
    Saída:
    - Lista de strings representando as equações paramétricas da reta.
    """
    if vetor is None:
        vetor = diferenca_vetores(pontoB, pontoA)

    equacoes = []
    for i in range(len(pontoA)):
        if vetor[i] < 0:
            equacoes.append(f"{chr(ord('x') + i)} = {pontoA[i]} - {abs(vetor[i])}t")
        else:
            equacoes.append(f"{chr(ord('x') + i)} = {pontoA[i]} + {vetor[i]}t")

    for eq in equacoes:
        print(eq)

    return equacoes


def equ_simetricas_reta(pontoA, pontoB, vetor):
    """
    Retorna a equação simétrica de uma reta passando por um ponto e seguindo uma direção.
    
    Entradas:
    - pontoA: lista de números representando o ponto inicial da reta.
    - pontoB: lista de números representando um segundo ponto da reta.
    - vetor: lista de números representando o vetor diretor da reta (opcional).
    
    Saída:
    - Lista de strings representando as equações simétricas da reta.
    
    Levanta:
    - ValueError: Se o vetor diretor tem componentes nulas.
    """
    if vetor is None:
        vetor = diferenca_vetores(pontoB, pontoA)

    if 0 in vetor:
        raise ValueError("O vetor não pode ter componentes nulas!")
    
    equacoes = []

    for i in range(len(vetor)):
        if pontoA[i] < 0:
            equacoes.append(f"{chr(ord('x') + i)} - {abs(pontoA[i])} / {vetor[i]}")
        else:
            equacoes.append(f"{chr(ord('x') + i)} - {abs(pontoA[i])} / {vetor[i]}")

    for eq in equacoes:
        print(eq)

    return equacoes


def pontos_em_reta_colinearidade(pontoA, pontoB, pontoC):
    """
    Verifica se três pontos estão em uma reta usando colinearidade.
    
    Entradas:
    - pontoA: lista de números representando o primeiro ponto.
    - pontoB: lista de números representando o segundo ponto.
    - pontoC: lista de números representando o terceiro ponto.
    
    Saída:
    - Booleano indicando se os pontos são colineares (True) ou não (False).
    """
    vet1 = diferenca_vetores(pontoB, pontoA)
    vet2 = diferenca_vetores(pontoC, pontoB)
    confirm = sao_colineares_angulo(vet1, vet2)
    return confirm


def pontos_em_reta_razao(pontoA, pontoB, pontoC):
    """
    Verifica se três pontos estão em uma reta usando razão.
    
    Entradas:
    - pontoA: lista de números representando o primeiro ponto.
    - pontoB: lista de números representando o segundo ponto.
    - pontoC: lista de números representando o terceiro ponto.
    
    Saída:
    - Booleano indicando se os pontos são colineares (True) ou não (False).
    """
    razao_inicial = (pontoB[0] - pontoA[0]) / (pontoC[0] - pontoA[0])
    for i in range(len(pontoA)):
        razao_atual = (pontoB[i] - pontoA[i]) / (pontoC[i] - pontoA[i])
        if razao_inicial != razao_atual:
            return False
    return True

#PAGINA 122

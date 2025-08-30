import random

# Variáveis globais
vida1 = 100
vida2 = 100
vida3 = 100
congelado1 = False
congelado2 = False
congelado3 = False
jogador1 = input("Digite o nome do primeiro jogador: ")
jogador2 = input("Digite o nome do segundo jogador: ")
jogador3 = input("Digite o nome do terceiro jogador: ")

def exibir_status():
    # Mostre o nome e a vida atual dos tres jogadores
    print(f"Jogador N1: {jogador1} Vida: {vida1}")
    print(f"Jogador N2: {jogador2} Vida: {vida2}")
    print(f"Jogador N3: {jogador3} Vida: {vida3}")

def escolher_magia():
    print("====MAGIAS====")
    print("1 - Bola de Fogo (15 - 30 de dano)")
    print("2 - Congelar (10 - 20 de dano + chance de congelar.)")
    print("3 - Cura (Recupera 10 - 25 pontos de vida.)")
    
    magia_escolhida = int(input("Escolha sua magia (1-3): "))
    if magia_escolhida in [1, 2, 3]:
        return magia_escolhida

def escolher_alvo(jogador_atual, magia_escolhida):
    
    print(f"Jogador N1: {jogador1} Vida: {vida1}")
    print(f"Jogador N2: {jogador2} Vida: {vida2}")
    print(f"Jogador N3: {jogador3} Vida: {vida3}")
    return int(input("Digite o número do jogador que deseja atacar: "))


def aplicar_bola_de_fogo(alvo):
    global vida1, vida2, vida3
    dano = random.randint(15, 30)
    if alvo == 1:
        vida1 -= dano
    elif alvo == 2:
        vida2 -= dano
    elif alvo == 3:
        vida3 -= dano
    print(f"O jogador {alvo} sofreu {dano} de dano da Bola de Fogo!")

def aplicar_raio_congelante(alvo):
    global vida1, vida2, vida3, congelado1, congelado2, congelado3
    dano = random.randint(10, 20)
    congelar = random.random() < 0.25
    if alvo == 1:
        vida1 -= dano
        if congelar:
            congelado1 = True
    elif alvo == 2:
        vida2 -= dano
        if congelar:
            congelado2 = True
    elif alvo == 3:
        vida3 -= dano
        if congelar:
            congelado3 = True
    print(f"O jogador {alvo} sofreu {dano} de dano do Raio Congelante!")
    if congelar:
        print(f"O jogador {alvo} foi CONGELADO!")

    # Sorteie o dano entre 10 e 20 e aplique ao alvo
    # Sorteie chance de congelar (25% de chance)
    # Se congelar, marque o alvo como congelado e informe ao jogador

def aplicar_cura(jogador):
    global vida1, vida2, vida3
    cura = random.randint(10, 25)
    if jogador == 1:
        vida1 = min(vida1 + cura, 100)
    elif jogador == 2:
        vida2 = min(vida2 + cura, 100)
    elif jogador == 3:
        vida3 = min(vida3 + cura, 100)
    print(f"O jogador {jogador} recuperou {cura} de vida!")
    # Sorteie o valor da cura entre 10 e 25
    # Some na vida do jogador (não pode passar de 100)
    # Mostre quanto foi recuperado

def turno(jogador_num):
    global congelado1, congelado2, congelado3
    # Verifique se o jogador está congelado → Se estiver, informe e remova o congelamento
    if jogador_num == 1:
        if congelado1:
            print(f"{jogador1} está congelado e perde o turno!")
            congelado1 = False
            return
        nome = jogador1
    elif jogador_num == 2:
        if congelado2:
            print(f"{jogador2} está congelado e perde o turno!")
            congelado2 = False
            return
        nome = jogador2
    elif jogador_num == 3:
        if congelado3:
            print(f"{jogador3} está congelado e perde o turno!")
            congelado3 = False
            return
        nome = jogador3
    # Caso contrário:
    # Execute a magia correta
    print(f"\nÉ a vez de {nome}")
    magia = escolher_magia()
    alvo = escolher_alvo(jogador_num, magia)
    if magia == 1:
        aplicar_bola_de_fogo(alvo)
    elif magia == 2:
        aplicar_raio_congelante(alvo)
    elif magia == 3:
        aplicar_cura(alvo)

# Programa Principal
print("=== Batalha de Magos ===")
# Peça os nomes dos jogadores

turno_num = 1

# Enquanto os dois jogadores estiverem vivos:
while sum([vida1 > 0, vida2 > 0, vida3 > 0]) > 1:
    print(f"\n===== TURNO {turno_num} =====")
    # Mostre o status
    exibir_status()
    if vida1 > 0:
        turno(1)
    if vida2 > 0:
        turno(2)
    if vida3 > 0:
        turno(3)
    # Execute o turno do Jogador 1
    # Verifique se o Jogador 2 ainda está vivo
    # Execute o turno do Jogador 2

    turno_num += 1

# Após o jogo terminar:
print("\n===== FIM DE JOGO =====")
# Mostre o status final
exibir_status()
# Informe quem venceu
if vida1 > 0:
    print(f"\n{jogador1} venceu!")
elif vida2 > 0:
    print(f"\n{jogador2} venceu!")
elif vida3 > 0:
    print(f"\n{jogador3} venceu!")
else:
    print("\nTodos perderam!")

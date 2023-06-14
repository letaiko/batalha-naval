import random
import time

# menu do jogo
print("☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼ BATALHA NAVAL ☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼")
nome = input("\ninsira seu nome: ")
#time.sleep(1)
#print(f"\nbem-vindo a batalha naval, {nome}! \npara ganhar, você deve adivinhar as posições das embarcações do computador!")
#time.sleep(3)
#print("\npronto?")
#time.sleep(1)
#print("vamos jogar!\n")

# tabuleiros fixos, tem as posições das embarcações!
mapacomputador = [
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ',],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ',],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ',],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ',],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ',],
]
mapajogador = [
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ',],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ',],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ',],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ',],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ',],

]
# tabuleiros que vão atualizando!
tabuleirocomputador = [
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ',],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ',],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ',],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ',],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ',],
]
tabuleirojogador = [
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ',],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ',],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ',],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ',],
  [' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ', ' ≈ ',],
]

embarcacoescomputador = 5
embarcacoesjogador = 5

# coleta posições embarcações jogador
for i in range(embarcacoesjogador):
  linhaposicao = int(input(f"\nInsira o número da linha da {i + 1} embarcação: "))
  while linhaposicao < 1 or linhaposicao > 5:
    linhaposicao = int(input("Linha inválida! Escolha uma linha de 1 a 5: "))
  colunaposicao = int(input(f"Insira o número da coluna da {i + 1} embarcação: "))
  while colunaposicao < 1 or colunaposicao > 10:
    colunaposicao = int(input("Coluna inválida! Escolha uma coluna de 1 a 10: "))
  mapajogador[linhaposicao - 1][colunaposicao - 1] = " x "

# gera randomicamente as posições das embarcações do computador
for i in range(embarcacoescomputador):
  linhaposicao = random.randint(0, 4)
  colunaposicao = random.randint(0, 9)

  # evita posições repetidas
  while mapacomputador[linhaposicao][colunaposicao] != ' ≈ ':
    linhacomputador = random.randint(0, 4)
    colunacomputador = random.randint(0, 9)

  mapacomputador[linhaposicao][colunaposicao] = " x "  

def jogada(mapa, tabuleiro, linha, coluna):
  if mapa[linha][coluna] == " x ":
    tabuleiro[linha][coluna] = " x "
    time.sleep(1)
    print("\n⚑ parabéns! acertou\n")
    return 1
    
  else:
    tabuleiro[linha][coluna] = " o "
    time.sleep(1)
    print("\n⚐ triste... errou\n")
    return 0

def imprimetabuleiros():
  # imprime tabuleiro do computador
  time.sleep(2)
  print("\n---- tabuleiro computador ----\n")
  for linha in range(5):
    print("".join(tabuleirocomputador[linha]))
  print("------------------------------")
  print(f"embarcações restantes: {embarcacoescomputador}")
  
  #  imprime tabuleiro do jogador
  time.sleep(1)
  print(f"\n\n----- tabuleiro {nome.casefold()} -----\n")
  for linha in range(5):
    print("".join(tabuleirojogador[linha]))
  print("------------------------------")
  print(f"embarcações restantes: {embarcacoesjogador}")
  time.sleep(3)
    
# começa o jogo
while embarcacoescomputador != 0 and embarcacoesjogador != 0:
  
  imprimetabuleiros()

  # recebe a jogada do jogador
  linhajogador = int(input("\n\n\ninsira a linha que deseja atacar: "))
  colunajogador = int(input("insira a coluna que deseja atacar: "))
  linhajogador -= 1
  colunajogador -= 1

  # evita jogadas inválidas
  while linhajogador < 0 or linhajogador > 4 or colunajogador < 0 or colunajogador > 9:
    print("\n\nposição inválida... insira uma linha (um valor de 1 a 5) e coluna (um valor de 1 a 10)!")
    linhajogador = int(input("\ninsira a linha que deseja atacar: "))
    colunajogador = int(input("insira a coluna que deseja atacar: "))
    linhajogador -= 1
    colunajogador -= 1
    
  # evita jogadas repetidas  
  while tabuleirocomputador[linhajogador][colunajogador] != ' ≈ ':
    print("\n\nposição já jogada... insira uma nova!")
    linhajogador = int(input("\ninsira a linha que deseja atacar: "))
    colunajogador = int(input("insira a coluna que deseja atacar: "))
    linhajogador -= 1
    colunajogador -= 1
  
  # checa jogada do jogador
  if jogada(mapacomputador, tabuleirocomputador, linhajogador, colunajogador) == 1:
    embarcacoescomputador -= 1

  imprimetabuleiros()

  if embarcacoescomputador == 0:
    break

  
  # recebe a jogada do computador
  linhacomputador = random.randint(0, 4)
  colunacomputador = random.randint(0, 9)

  # evitar jogadas repetidas
  while tabuleirojogador[linhacomputador][colunacomputador] != ' ≈ ':
    linhacomputador = random.randint(0, 4)
    colunacomputador = random.randint(0, 9)
  
  print(f"\n\n\ncomputador escolheu linha {linhacomputador + 1}")
  time.sleep(3)
  print(f"computador escolheu coluna {colunacomputador + 1}")

  # checa jogada do computador
  if jogada(mapajogador, tabuleirojogador, linhacomputador, colunacomputador) == 1:
    embarcacoesjogador -= 1



# verifica o vencedor
if embarcacoescomputador == 0:
  vencedor = nome
if embarcacoesjogador == 0:
  vencedor = "COMPUTADOR"

print("\n\n≋≋≋≋≋≋≋≋≋≋≋≋≋≋ FIM DE JOGO ≋≋≋≋≋≋≋≋≋≋≋≋≋≋")
time.sleep(1)
print(f"\n             ♆ {vencedor.upper()} VENCEU ♆")
print(f"\n\nobrigada por jogar, {nome.capitalize()}!")
print("\njogo desenvolvido por: Anna, Andressa, Letícia, Michele e Yejin")

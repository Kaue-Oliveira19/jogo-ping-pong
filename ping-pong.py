
#Bibliotecas utilizadas para desenvolver o jogo
import pygame
import random
pygame.init()

#Inicializa os módulos da biblioteca e define o título do programa
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Ping Pong")

#Variáveis com RGB das cores
cinza_escuro = (40, 40, 40)
azul_mesa = (30, 80, 160)
azul_claro = (40, 100, 190)
branco = (255, 255, 255)
cinza_claro = (200, 200, 200)
azul_raquete = (0, 0, 200)
vermelho_raquete = (200, 0, 0)
marrom = (120, 70, 30)
laranja = (220, 100, 30)

#Variáveis que definem a posição x e y dos objetos da tela (Tamanho dos objetos), e a velocida da raquete
jogador1_y = 150
jogador2_y = 150
tam_raquete_x = 12
tam_raquete_y = 80
vel_raquete = 7

#Defini a posição em que a bola irá aparecer e o tamanho da bola
bola_x = largura // 2
bola_y = altura // 2
bola_vel_x = random.choice([-5, -4, 4, 5])
bola_vel_y = random.choice([-5, -4, 4, 5])
tamanho_bola = 7

#Defini a a pontuação, o tamanho da fontes dos textos usados na tela e o FPS
pontos1 = 0
pontos2 = 0
fonte = pygame.font.Font(None, 36)
fonte_pequena = pygame.font.Font(None, 22)
clock = pygame.time.Clock()
rodando = True

#Loop onde o jogo irá rodar
while rodando:

    #Verifica se o jogo foi fechado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    #Variável que armazena qual tecla o usuário digitou
    teclas = pygame.key.get_pressed()

    #Verifica qual tecla o usuário apertou e defini a posição do jogador
    if teclas[pygame.K_w]:
        jogador1_y = jogador1_y - vel_raquete
    if teclas[pygame.K_s]:
        jogador1_y = jogador1_y + vel_raquete

    if teclas[pygame.K_UP]:
        jogador2_y = jogador2_y - vel_raquete
    if teclas[pygame.K_DOWN]:
        jogador2_y = jogador2_y + vel_raquete

    #Impede que a raquete ultrapasse o limite da tela
    if jogador1_y < 30:
        jogador1_y = 30
    if jogador1_y > altura - tam_raquete_y - 30:
        jogador1_y = altura - tam_raquete_y - 30

    #Impede que a raquete ultrapasse o limite da tela
    if jogador2_y < 30:
        jogador2_y = 30
    if jogador2_y > altura - tam_raquete_y - 30:
        jogador2_y = altura - tam_raquete_y - 30

    #Equeção de movimento da bola
    bola_x = bola_x + bola_vel_x
    bola_y = bola_y + bola_vel_y

    if bola_y <= 30 or bola_y >= altura - 30 - tamanho_bola:
        bola_vel_y = bola_vel_y * -1

    if bola_x <= 55 + tam_raquete_x:
        if bola_y + tamanho_bola >= jogador1_y and bola_y <= jogador1_y + tam_raquete_y:
            bola_vel_x = bola_vel_x * -1
            bola_x = 55 + tam_raquete_x + 1
            if random.randint(0, 3) == 0:
                bola_vel_y = bola_vel_y + random.choice([-1, 1])

    if bola_x + tamanho_bola >= largura - 55 - tam_raquete_x:
        if bola_y + tamanho_bola >= jogador2_y and bola_y <= jogador2_y + tam_raquete_y:
            bola_vel_x = bola_vel_x * -1
            bola_x = largura - 55 - tam_raquete_x - tamanho_bola - 1

    #Ocorre uma verificação se o jogador (Vermelho) pontou e redefini a posição da bola
    if bola_x < 0:
        pontos2 = pontos2 + 1
        bola_x = largura // 2
        bola_y = altura // 2
        bola_vel_x = random.choice([-4, 4])
        bola_vel_y = random.choice([-4, 4])
        print(f"Ponto pro vermelho! {pontos1} x {pontos2}")

    #Ocorre uma verificação se o jogador (Azul) pontou e redefini a posição da bola
    if bola_x > largura:
        pontos1 = pontos1 + 1
        bola_x = largura // 2
        bola_y = altura // 2
        bola_vel_x = random.choice([-4, 4])
        bola_vel_y = random.choice([-4, 4])
        print(f"Ponto pro azul! {pontos1} x {pontos2}")

    #Preenche a tela com a cor selecionada
    tela.fill(cinza_escuro)

    #Defini as cores intercaladas do fundo do jogo
    faixa = 0
    while faixa < 6:
        if faixa % 2 == 0:
            pygame.draw.rect(tela, azul_claro, (faixa * 100, 30, 100, altura - 60))
        else:
            pygame.draw.rect(tela, azul_mesa, (faixa * 100, 30, 100, altura - 60))
        faixa = faixa + 1

    pygame.draw.rect(tela, branco, (0, 30, largura, altura - 60), 3)

    pygame.draw.line(tela, branco, (largura // 2, 30), (largura // 2, altura - 30), 2)

    #Defini a posição da rede que fica no meio da tela
    rede_y = 30
    while rede_y < altura - 30:
        if (rede_y // 10) % 2 == 0:
            pygame.draw.rect(tela, branco, (largura // 2 - 4, rede_y, 8, 10))
        else:
            pygame.draw.rect(tela, cinza_claro, (largura // 2 - 4, rede_y, 8, 10))
        rede_y = rede_y + 10

    #Cria os objetos e defini a sua posição tela
    pygame.draw.rect(tela, cinza_claro, (largura // 2 - 2, 25, 4, altura - 50))

    pygame.draw.rect(tela, marrom, (40, jogador1_y + tam_raquete_y // 2 - 5, 18, 10))

    pygame.draw.rect(tela, azul_raquete, (55, jogador1_y, tam_raquete_x, tam_raquete_y))

    pygame.draw.rect(tela, branco, (55, jogador1_y, tam_raquete_x, tam_raquete_y), 1)

    pygame.draw.rect(tela, marrom, (largura - 58, jogador2_y + tam_raquete_y // 2 - 5, 18, 10))

    pygame.draw.rect(tela, vermelho_raquete, (largura - 55 - tam_raquete_x, jogador2_y, tam_raquete_x, tam_raquete_y))

    pygame.draw.rect(tela, branco, (largura - 55 - tam_raquete_x, jogador2_y, tam_raquete_x, tam_raquete_y), 1)

    pygame.draw.circle(tela, laranja, (int(bola_x), int(bola_y)), tamanho_bola)
    pygame.draw.circle(tela, branco, (int(bola_x) - 2, int(bola_y) - 2), 2)

    #Defini a posição da pontuação dos players
    texto1 = fonte.render(str(pontos1), True, branco)
    texto2 = fonte.render(str(pontos2), True, branco)
    tela.blit(texto1, (150, 5))
    tela.blit(texto2, (440, 5))

    #Defini o nome e a posição dos nomes dos players
    nome1 = fonte_pequena.render("J1", True, azul_raquete)
    nome2 = fonte_pequena.render("J2", True, vermelho_raquete)
    tela.blit(nome1, (120, 8))
    tela.blit(nome2, (470, 8))

    #Mostra a visualização da tela e fixa o FPS em 60
    pygame.display.flip()
    clock.tick(60)

#Fecha a janela do jogo
pygame.quit()
print("Saindo...")

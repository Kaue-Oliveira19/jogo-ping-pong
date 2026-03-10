import pygame
import random

pygame.init()

largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Ping Pong")

preto = (0, 0, 0)
branco = (255, 255, 255)
azul = (0, 0, 255)  
vermelho = (255, 0, 0) 

jogador1_y = 150  
jogador2_y = 150
tam_raquete_x = 10
tam_raquete_y = 100
vel_raquete = 7

bola_x = largura // 2
bola_y = altura // 2
bola_vel_x = random.choice([-5, -4, 4, 5]) 
bola_vel_y = random.choice([-5, -4, 4, 5])
tamanho_bola = 8  

pontos1 = 0
pontos2 = 0
fonte = pygame.font.Font(None, 30)  

clock = pygame.time.Clock()

rodando = True

while rodando:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_w]:
        jogador1_y = jogador1_y - vel_raquete
    if teclas[pygame.K_s]:
        jogador1_y = jogador1_y + vel_raquete
    
    if teclas[pygame.K_UP]:
        jogador2_y = jogador2_y - vel_raquete
    if teclas[pygame.K_DOWN]:
        jogador2_y = jogador2_y + vel_raquete
    
    if jogador1_y < 0:
        jogador1_y = 0
    if jogador1_y > altura - tam_raquete_y:
        jogador1_y = altura - tam_raquete_y
    
    if jogador2_y < 0:
        jogador2_y = 0
    if jogador2_y > altura - tam_raquete_y:
        jogador2_y = altura - tam_raquete_y
    
    bola_x = bola_x + bola_vel_x
    bola_y = bola_y + bola_vel_y
    
    if bola_y <= 0 or bola_y >= altura - tamanho_bola:
        bola_vel_y = bola_vel_y * -1  
    
    if bola_x <= tam_raquete_x:
        if bola_y + tamanho_bola >= jogador1_y and bola_y <= jogador1_y + tam_raquete_y:
            bola_vel_x = bola_vel_x * -1
            bola_x = tam_raquete_x + 1  
            if random.randint(1, 10) > 7:
                bola_vel_x = bola_vel_x * 1.2
                bola_vel_y = bola_vel_y * 1.2
    
    if bola_x + tamanho_bola >= largura - tam_raquete_x:
        if bola_y + tamanho_bola >= jogador2_y and bola_y <= jogador2_y + tam_raquete_y:
            bola_vel_x = bola_vel_x * -1
            bola_x = largura - tam_raquete_x - tamanho_bola - 1
            if random.randint(1, 10) > 7:
                bola_vel_x = bola_vel_x * 1.2
                bola_vel_y = bola_vel_y * 1.2
    
    if bola_x < 0:
        pontos2 = pontos2 + 1
        bola_x = largura // 2
        bola_y = altura // 2
        bola_vel_x = random.choice([-4, 4])
        bola_vel_y = random.choice([-4, 4])
        print(f"Ponto pro vermelho! {pontos1} x {pontos2}")
    
    if bola_x > largura:
        pontos1 = pontos1 + 1
        bola_x = largura // 2
        bola_y = altura // 2
        bola_vel_x = random.choice([-4, 4])
        bola_vel_y = random.choice([-4, 4])
        print(f"Ponto pro azul! {pontos1} x {pontos2}")
    
    tela.fill(preto)  
    
    pygame.draw.rect(tela, azul, (0, jogador1_y, tam_raquete_x, tam_raquete_y))

    pygame.draw.rect(tela, vermelho, (largura - tam_raquete_x, jogador2_y, tam_raquete_x, tam_raquete_y))
    
    pygame.draw.circle(tela, branco, (int(bola_x), int(bola_y)), tamanho_bola)
    
    texto1 = fonte.render(str(pontos1), True, azul)
    texto2 = fonte.render(str(pontos2), True, vermelho)
    tela.blit(texto1, (150, 20))
    tela.blit(texto2, (450, 20))
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
print("Saindo...")
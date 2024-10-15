import pygame
import time
import random

# Inicializar Pygame
pygame.init()

# Colores
blanco = (255, 255, 255)
amarillo = (255, 255, 102)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Dimensiones de la pantalla
ancho = 600
alto = 400

pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Snake Game')

reloj = pygame.time.Clock()
tamaño_cuadro = 10
velocidad_snake = 15

fuente = pygame.font.SysFont(None, 35)

def mostrar_puntuacion(puntuacion):
    texto = fuente.render(f"Puntuación: {puntuacion}", True, negro)
    pantalla.blit(texto, [0, 0])

def dibujar_snake(tamaño_cuadro, lista_snake):
    for x in lista_snake:
        pygame.draw.rect(pantalla, verde, [x[0], x[1], tamaño_cuadro, tamaño_cuadro])

def mensaje(msg, color):
    texto = fuente.render(msg, True, color)
    pantalla.blit(texto, [ancho / 6, alto / 3])

def juego():
    game_over = False
    game_close = False

    x1 = ancho / 2
    y1 = alto / 2

    x1_cambio = 0
    y1_cambio = 0

    lista_snake = []
    longitud_snake = 1

    comida_x = round(random.randrange(0, ancho - tamaño_cuadro) / 10.0) * 10.0
    comida_y = round(random.randrange(0, alto - tamaño_cuadro) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            pantalla.fill(azul)
            mensaje("Perdiste! Presiona C para continuar o Q para salir", rojo)
            mostrar_puntuacion(longitud_snake - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        juego()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_cambio = -tamaño_cuadro
                    y1_cambio = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_cambio = tamaño_cuadro
                    y1_cambio = 0
                elif evento.key == pygame.K_UP:
                    y1_cambio = -tamaño_cuadro
                    x1_cambio = 0
                elif evento.key == pygame.K_DOWN:
                    y1_cambio = tamaño_cuadro
                    x1_cambio = 0

        if x1 >= ancho or x1 < 0 or y1 >= alto or y1 < 0:
            game_close = True

        x1 += x1_cambio
        y1 += y1_cambio
        pantalla.fill(azul)
        pygame.draw.rect(pantalla, amarillo, [comida_x, comida_y, tamaño_cuadro, tamaño_cuadro])
        cabeza_snake = []
        cabeza_snake.append(x1)
        cabeza_snake.append(y1)
        lista_snake.append(cabeza_snake)
        if len(lista_snake) > longitud_snake:
            del lista_snake[0]

        for x in lista_snake[:-1]:
            if x == cabeza_snake:
                game_close = True

        dibujar_snake(tamaño_cuadro, lista_snake)
        mostrar_puntuacion(longitud_snake - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ancho - tamaño_cuadro) / 10.0) * 10.0
            comida_y = round(random.randrange(0, alto - tamaño_cuadro) / 10.0) * 10.0
            longitud_snake += 1

        reloj.tick(velocidad_snake)

    pygame.quit()
    quit()

if __name__ == "__main__":
    juego()


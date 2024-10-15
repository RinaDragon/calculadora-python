import pygame
import random

# Inicializar pygame
pygame.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Carrera de Buses")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Clase Bus
class Bus:
    def __init__(self, x, y):
        self.image = pygame.Surface((50, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = random.randint(1, 5)

    def move(self):
        self.rect.y -= self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Función principal
def main():
    clock = pygame.time.Clock()
    buses = [Bus(random.randint(100, WIDTH-100), random.randint(HEIGHT-100, HEIGHT)) for _ in range(5)]
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        for bus in buses:
            bus.move()
            if bus.rect.bottom < 0:
                bus.rect.y = HEIGHT
                bus.rect.x = random.randint(100, WIDTH - 100)
            bus.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

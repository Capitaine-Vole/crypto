import pygame

WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crypto")

clock = pygame.time.Clock()
run = True

while run:

    clock.tick(60)

    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()

    pygame.display.update()
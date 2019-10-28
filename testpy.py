import pygame

pygame.init()
screen = pygame.display.set_mode((500, 300))
running = True
is_blue = True

while running:
    if is_blue: color = (0,128,255)
    else: color = (255,100,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
    # drawing a rect
    pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))

    pygame.display.flip()
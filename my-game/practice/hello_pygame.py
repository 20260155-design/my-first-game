import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

char_radius = 25
char_x = SCREEN_WIDTH // 2
char_y = SCREEN_HEIGHT // 2
Gray = (200, 200, 200)
base_speed = 5

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    is_dashing = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]

    if is_dashing:
        current_speed = base_speed * 2
    else:
        current_speed = base_speed

    if keys[pygame.K_LEFT]:
        char_x -= current_speed
    if keys[pygame.K_RIGHT]:
        char_x += current_speed
    if keys[pygame.K_UP]:
        char_y -= current_speed
    if keys[pygame.K_DOWN]:
        char_y += current_speed            
            
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, Gray, (int(char_x), int(char_y)), char_radius)
    
    pygame.display.update()           

pygame.quit()

import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Поймай яблоко")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)

player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 10

apple_size = 30
apple_x = random.randint(0, WIDTH - apple_size)
apple_y = 0
apple_speed = 5

score = 0
font = pygame.font.SysFont("Arial", 30)

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    win.fill(WHITE)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    apple_y += apple_speed
    if apple_y > HEIGHT:
        apple_y = 0
        apple_x = random.randint(0, WIDTH - apple_size)

    if (player_x < apple_x + apple_size and
        player_x + player_size > apple_x and
        player_y < apple_y + apple_size and
        player_y + player_size > apple_y):
        score += 1
        apple_y = 0
        apple_x = random.randint(0, WIDTH - apple_size)

    pygame.draw.rect(win, GREEN, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(win, RED, (apple_x, apple_y, apple_size, apple_size))
    score_text = font.render(f"Счёт: {score}", True, (0, 0, 0))
    win.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
import pygame
import random

pygame.init()

# game res
WIDTH = 600
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Save Water Game")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

player_width = 50
player_height = 50
player_x = (WIDTH - player_width) // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Raindrop properties
raindrop_width = 20
raindrop_height = 20
raindrop_x = random.randint(0, WIDTH - raindrop_width)
raindrop_y = -raindrop_height
raindrop_speed = 3

# Red raindrop properties
red_raindrop_width = 20
red_raindrop_height = 20
red_raindrop_x = random.randint(0, WIDTH - red_raindrop_width)
red_raindrop_y = -red_raindrop_height
red_raindrop_speed = 5

score = 0
font = pygame.font.Font(None, 36)

# start game
running = True
clock = pygame.time.Clock()

def draw_player():
    pygame.draw.rect(window, BLUE, (player_x, player_y, player_width, player_height))

def draw_raindrop():
    pygame.draw.rect(window, WHITE, (raindrop_x, raindrop_y, raindrop_width, raindrop_height))

def draw_red_raindrop():
    pygame.draw.rect(window, RED, (red_raindrop_x, red_raindrop_y, red_raindrop_width, red_raindrop_height))

def show_score():
    score_text = font.render("Score: " + str(score), True, RED)
    window.blit(score_text, (10, 10))

def handle_collision():
    global score, running
    if player_x < raindrop_x + raindrop_width and player_x + player_width > raindrop_x and player_y < raindrop_y + raindrop_height and player_y + player_height > raindrop_y:
        score += 1
        return True
    elif player_x < red_raindrop_x + red_raindrop_width and player_x + player_width > red_raindrop_x and player_y < red_raindrop_y + red_raindrop_height and player_y + player_height > red_raindrop_y:
        running = False
    return False

while running:
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    raindrop_y += raindrop_speed
    red_raindrop_y += red_raindrop_speed

    if raindrop_y > HEIGHT:
        raindrop_x = random.randint(0, WIDTH - raindrop_width)
        raindrop_y = -raindrop_height

    if red_raindrop_y > HEIGHT:
        red_raindrop_x = random.randint(0, WIDTH - red_raindrop_width)
        red_raindrop_y = -red_raindrop_height

    if handle_collision():
        raindrop_x = random.randint(0, WIDTH - raindrop_width)
        raindrop_y = -raindrop_height

    draw_player()
    draw_raindrop()
    draw_red_raindrop()
    show_score()

    pygame.display.update()
    clock.tick(90)

pygame.quit()

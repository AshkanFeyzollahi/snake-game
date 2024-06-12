"""snake-game

The snake-game which made in Python3 using Pygame."""

import pygame
from random import randrange

WINDOW_SIZE: int = 600
TILE_SIZE: float = WINDOW_SIZE / 20
RANGE: tuple[int] = (TILE_SIZE // 2, WINDOW_SIZE - TILE_SIZE // 2, TILE_SIZE)

generate_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]

snake: pygame.Rect = pygame.Rect(0, 0, TILE_SIZE - 2, TILE_SIZE - 2)
snake.center = generate_random_position()
snake_length: int = 1
segments: list[pygame.Rect] = [snake.copy()]
snake_direction: tuple[int] = (0, 0)

food = snake.copy()
food.center = generate_random_position()

pygame.display.set_caption("Snake Game")
screen: pygame.Surface = pygame.display.set_mode([WINDOW_SIZE] * 2)

clock: pygame.time.Clock = pygame.time.Clock()
time, time_step = 0, 110

def restart():
    global snake_length
    snake_length = 1
    global segments
    segments = [snake.copy()]
    global snake_direction
    snake_direction = (0, 0)
    food.center = generate_random_position()
    snake.center = generate_random_position()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()

            if event.key == pygame.K_w and snake_direction != (0, TILE_SIZE):
                snake_direction = (0, -TILE_SIZE)
                break

            if event.key == pygame.K_s and snake_direction != (0, -TILE_SIZE):
                snake_direction = (0, TILE_SIZE)
                break

            if event.key == pygame.K_a and snake_direction != (TILE_SIZE, 0):
                snake_direction = (-TILE_SIZE, 0)
                break

            if event.key == pygame.K_d and snake_direction != (-TILE_SIZE, 0):
                snake_direction = (TILE_SIZE, 0)
                break

            if event.key == pygame.K_UP and snake_direction != (0, TILE_SIZE):
                snake_direction = (0, -TILE_SIZE)
                break

            if event.key == pygame.K_DOWN and snake_direction != (0, -TILE_SIZE):
                snake_direction = (0, TILE_SIZE)
                break

            if event.key == pygame.K_LEFT and snake_direction != (TILE_SIZE, 0):
                snake_direction = (-TILE_SIZE, 0)
                break

            if event.key == pygame.K_RIGHT and snake_direction != (-TILE_SIZE, 0):
                snake_direction = (TILE_SIZE, 0)
                break

    screen.fill('black')
    
    pygame.draw.rect(screen, 'red', food)
    [pygame.draw.rect(screen, 'green', segment) for segment in segments]

    if snake.center[0] > WINDOW_SIZE or snake.center[1] > WINDOW_SIZE \
        or snake.center[0] < 0 or snake.center[1] < 0:
        restart()
    
    if snake.collidelist(segments[:-1]) != -1:
        restart()
    
    if snake.center == food.center:
        snake_length += 1
        food.center = generate_random_position()
    
    time_now = pygame.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_direction)
        segments.append(snake.copy())
        segments = segments[-snake_length:]
    
    pygame.display.flip()
    clock.tick(60)

import pygame
import sys
import random

# تنظیمات بازی
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
SNAKE_SPEED = 10

# رنگ‌ها
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# تعریف توابع
def draw_grid(surface):
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(surface, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(surface, WHITE, (0, y), (WIDTH, y))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("بازی مار مرحله‌ای")

    snake = [(5, 5)]
    snake_direction = (1, 0)
    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    score = 0

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != (0, 1):
                    snake_direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                    snake_direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                    snake_direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                    snake_direction = (1, 0)

        snake_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])

        if snake_head == food:
            snake.append(food)
            score += 1
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        else:
            snake.pop()

        if (
            snake_head in snake[1:] or
            snake_head[0] < 0 or snake_head[0] >= GRID_WIDTH or
            snake_head[1] < 0 or snake_head[1] >= GRID_HEIGHT
        ):
            pygame.quit()
            sys.exit()

        screen.fill((0, 0, 0))
        draw_grid(screen)

        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        pygame.display.update()
        clock.tick(SNAKE_SPEED)

if __name__ == "__main__":
    main()

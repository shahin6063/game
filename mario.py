import pygame
import sys

# تنظیمات بازی
WIDTH, HEIGHT = 640, 480
SCREEN_SIZE = (WIDTH, HEIGHT)
BACKGROUND_COLOR = (0, 0, 255)  # آبی
CHARACTER_COLOR = (255, 0, 0)   # قرمز

# تعریف توابع
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("بازی ماریو مرحله‌ای")

    character_size = (30, 30)
    character_x = WIDTH // 2 - character_size[0] // 2
    character_y = HEIGHT - character_size[1] - 10
    character_speed = 5

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character_x -= character_speed
        if keys[pygame.K_RIGHT]:
            character_x += character_speed

        # حد مرزهای صفحه را در نظر بگیرید
        if character_x < 0:
            character_x = 0
        if character_x > WIDTH - character_size[0]:
            character_x = WIDTH - character_size[0]

        # رسم ماریو
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, CHARACTER_COLOR, (character_x, character_y, character_size[0], character_size[1]))

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
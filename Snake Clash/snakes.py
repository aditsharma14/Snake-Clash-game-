import pygame
import random
import os

pygame.init()
pygame.mixer.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
medium_blue = (0, 191, 255)
blue = (0, 0, 255)

# Screen
screen_width = 900
screen_height = 600

# Game window
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SNAKE CLASH")

# Base path for assets
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# Background image
bgimg_path = os.path.join(BASE_DIR, "snake_bg.jpg")
bgimg = pygame.image.load(bgimg_path)
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height))

# Sounds
eat_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "eat.mp3"))
gameover_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "game_over.mp3"))

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def welcome():
    exit_game = False

    while not exit_game:

        gameWindow.blit(bgimg, (0, 0))

        text_screen("WELCOME TO SNAKE CLASH", red, 210, 200)
        text_screen("Press SPACE to Play", yellow, 280, 270)
        text_screen("Arrow Keys = Move", medium_blue, 280, 340)
        text_screen("P = Pause Game", medium_blue, 310, 390)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(60)


def gameloop():

    exit_game = False
    game_over = False
    paused = False

    snake_x = 45
    snake_y = 55

    velocity_x = 0
    velocity_y = 0

    snake_size = 20
    init_velocity = 20

    fps = 10

    score = 0

    snk_list = []
    snk_length = 1

    # Food generation
    food_x = random.randint(20, screen_width - 40)
    food_y = random.randint(20, screen_height - 40)

    food_type = random.choice(["normal", "bonus", "slow"])

    # Load high score
    hiscore_path = os.path.join(BASE_DIR, "hiscore.txt")
    try:
        with open(hiscore_path, "r") as f:
            hiscore = f.read()

    except FileNotFoundError:

        with open(hiscore_path, "w") as f:
            f.write("0")

        hiscore = "0"

    while not exit_game:

        if game_over:

            with open(hiscore_path, "w") as f:
                f.write(str(hiscore))

            gameWindow.blit(bgimg, (0, 0))

            text_screen("GAME OVER", red, 300, 220)
            text_screen("Press ENTER to Restart", white, 230, 300)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        return gameloop()

        else:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:

                    # Pause
                    if event.key == pygame.K_p:
                        paused = not paused

                    if not paused:

                        # Movement controls
                        if event.key == pygame.K_RIGHT and velocity_x != -init_velocity:
                            velocity_x = init_velocity
                            velocity_y = 0

                        if event.key == pygame.K_LEFT and velocity_x != init_velocity:
                            velocity_x = -init_velocity
                            velocity_y = 0

                        if event.key == pygame.K_UP and velocity_y != init_velocity:
                            velocity_y = -init_velocity
                            velocity_x = 0

                        if event.key == pygame.K_DOWN and velocity_y != -init_velocity:
                            velocity_y = init_velocity
                            velocity_x = 0

            # Pause Screen
            if paused:

                gameWindow.blit(bgimg, (0, 0))

                overlay = pygame.Surface((screen_width, screen_height))
                overlay.set_alpha(120)
                overlay.fill((0, 0, 0))

                gameWindow.blit(overlay, (0, 0))

                text_screen("PAUSED", medium_blue, 360, 240)
                text_screen("Press P to Resume", white, 280, 310)

                pygame.display.update()
                clock.tick(15)
                continue

            # Snake movement
            snake_x += velocity_x
            snake_y += velocity_y

            # Collision rectangles
            snake_rect = pygame.Rect(
                snake_x,
                snake_y,
                snake_size,
                snake_size
            )

            food_rect = pygame.Rect(
                food_x,
                food_y,
                snake_size,
                snake_size
            )

            # Eating food
            if snake_rect.colliderect(food_rect):

                if food_type == "normal":
                    score += 10
                    eat_sound.play()

                elif food_type == "bonus":
                    score += 50
                    eat_sound.play()

                elif food_type == "slow":
                    fps = 4
                    eat_sound.play()

                # New food generation
                food_x = random.randint(20, screen_width - 40)
                food_y = random.randint(20, screen_height - 40)

                food_type = random.choice(
                    ["normal", "bonus", "slow"]
                )

                snk_length += 5

                if score > int(hiscore):
                    hiscore = score

            # Draw background
            gameWindow.blit(bgimg, (0, 0))

            # Score display
            text_screen(
                "Score: " + str(score) +
                "  High Score: " + str(hiscore),
                red,
                10,
                10,
            )

            # Snake Head
            head = [snake_x, snake_y]
            snk_list.append(head)

            # Snake length control
            if len(snk_list) > snk_length:
                del snk_list[0]

            # Self collision
            if head in snk_list[:-1]:
                game_over = True
                gameover_sound.play()

            # Wall collision
            if (
                snake_x < 0
                or snake_x > screen_width
                or snake_y < 0
                or snake_y > screen_height
            ):
                game_over = True
                gameover_sound.play()

            # Food colors
            if food_type == "normal":
                food_color = black

            elif food_type == "bonus":
                food_color = red

            elif food_type == "slow":
                food_color = blue

            # Draw food
            pygame.draw.rect(
                gameWindow,
                food_color,
                [food_x, food_y, snake_size, snake_size],
                border_radius=6,
            )

            # Draw snake body
            for segment in snk_list[:-1]:

                pygame.draw.rect(
                    gameWindow,
                    yellow,
                    [segment[0], segment[1], snake_size, snake_size],
                    border_radius=6,
                )

            # Draw snake head
            pygame.draw.rect(
                gameWindow,
                green,
                [head[0], head[1], snake_size, snake_size],
                border_radius=6,
            )

            # Snake eyes
            pygame.draw.circle(
                gameWindow,
                black,
                (head[0] + 5, head[1] + 5),
                2
            )

            pygame.draw.circle(
                gameWindow,
                black,
                (head[0] + 14, head[1] + 5),
                2
            )

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()
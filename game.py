import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CAR_WIDTH, CAR_HEIGHT = 50, 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Racing Game")

 Load car image
car_image = pygame.image.load("car.png")
car_image = pygame.transform.scale(car_image, (CAR_WIDTH, CAR_HEIGHT))

# Set up the player's car
player_x = WIDTH // 2 - CAR_WIDTH // 2
player_y = HEIGHT - CAR_HEIGHT - 20
player_speed = 5

# Create a list of obstacles
obstacles = []
obstacle_speed = 5
obstacle_width = 50
obstacle_height = 50

# Game loop
clock = pygame.time.Clock()
running = True

score = 0

def draw_player_car(x, y):
    screen.blit(car_image, (x, y))

def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLACK, obstacle)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    screen.fill(WHITE)

    # Spawn obstacles
    if random.randint(0, 100) < 2:
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
        obstacle_y = 0
        obstacles.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # Move obstacles
    for obstacle in obstacles:
        obstacle.move_ip(0, obstacle_speed)

    # Remove obstacles that have gone off the screen
    obstacles = [obstacle for obstacle in obstacles if obstacle.y < HEIGHT]

    # Check for collisions
    player_rect = pygame.Rect(player_x, player_y, CAR_WIDTH, CAR_HEIGHT)
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            running = False

    # Draw player's car
    draw_player_car(player_x, player_y)

    # Draw obstacles
    draw_obstacles(obstacles)

    # Update the display
    pygame.display.update()

    # Increase the score
    score += 1

    # Limit frame rate
    clock.tick(60)

# Game over screen
font = pygame.font.Font(None, 36)
game_over_text = font.render("Game Over", True, BLACK)
score_text = font.render(f"Score: {score}", True, BLACK)
screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
screen.blit(score_text, (WIDTH // 2 - 60, HEIGHT // 2))
pygame.display.update()

# Wait for a few seconds before closing the game
pygame.time.wait(2000)

# Quit Pygame
pygame.quit()

import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
zombie_pos_start = pygame.Vector2(-1000 * random.randint(-1, 1), -1000 * random.randint(-1, 1))

def player_movement():
    pygame.draw.circle(screen, "red", player_pos, 40)

    hitbox = pygame.Rect(player_pos, (50, 50))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 600 * dt
    if keys[pygame.K_s]:
        player_pos.y += 600 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 600 * dt
    if keys[pygame.K_d]:
        player_pos.x += 600 * dt

    if player_pos.x > screen.get_width() or player_pos.y > screen.get_height():
            pygame.quit()
    if player_pos.x < 0 or player_pos.y < 0:
            pygame.quit()
    return hitbox

def zombie_movement(zombie_pos, player_pos_current, player_hitbox):
    zombie_pos = zombie_pos.move_towards(player_pos_current, 11)
    pygame.draw.circle(screen, "green", zombie_pos, 40)
    zombie_hitbox = pygame.Rect(zombie_pos, (50, 50))
    collision = pygame.Rect.colliderect(player_hitbox, zombie_hitbox)
    if collision:
        pygame.quit()

    return zombie_pos

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    player_hitbox = player_movement()

    zombie_pos_start = zombie_movement(zombie_pos_start, player_pos, player_hitbox)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
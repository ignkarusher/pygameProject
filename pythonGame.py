# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
zombie_pos_start = pygame.Vector2(player_pos.x + random.randint(-600, 600), player_pos.y + random.randint(-600, 600))


def player_mouvement():
    pygame.draw.circle(screen, "red", player_pos, 40)

    hitbox = pygame.Rect((player_pos), (50, 50))

    # collision = pygame.Rect.colliderect(hitbox, player_pos)

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
    return hitbox

def zombie_mouvement(zombie_pos, player_pos_current, player_hitbox):
    zombie_pos = zombie_pos.move_towards(player_pos_current, 8)
    pygame.draw.circle(screen, "green", zombie_pos, 40)
    zombie_hitbox = pygame.Rect(zombie_pos, (50, 50))
    collision = pygame.Rect.colliderect(player_hitbox, zombie_hitbox)
    if collision:
        pygame.quit()

    return zombie_pos

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    player_hitbox = player_mouvement()

    zombie_pos_start=zombie_mouvement(zombie_pos_start, player_pos, player_hitbox)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
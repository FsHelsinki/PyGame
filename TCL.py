import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores



def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Alien war")
    bg_color = (0, 0, 0)
    bg = pygame.image.load('images/fone.png')
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)
    rect = bg.get_rect()

    while True:
        screen.blit(bg, rect)
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, inos, bullets)
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, sc, gun, inos, bullets)
        pygame.display.flip()
run()

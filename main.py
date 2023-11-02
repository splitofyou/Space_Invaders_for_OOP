import pygame, controls
from main_character import MainCharacter
from pygame.sprite import Group
from stats import Stats


def start_game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 900))
    pygame.display.set_caption("WAY2DIE")

    
    maincharacter = MainCharacter(screen)
    bullets = Group()
    # enemy = Enemy(screen)
    enemys = Group()

    controls.create_army(screen, enemys)
    bg = pygame.image.load("images/bg.png")
    screen.blit(bg, (0, 0))

    stats = Stats()
    flag = True
    while flag:
        controls.events(screen, maincharacter, bullets)
        maincharacter.output()
        pygame.display.flip()
        maincharacter.moving(screen)

        controls.update(screen, maincharacter, enemys, bullets)
        controls.update_bullets(screen, enemys,bullets)
        controls.update_enemys(stats, screen, maincharacter, enemys, bullets)

start_game()

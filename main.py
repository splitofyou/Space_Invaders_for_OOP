import pygame
import sys
from main_character import MainCharacter
def start_game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("WAY2DIE")
    maincharacter = MainCharacter(screen)

    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    maincharacter.move_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    maincharacter.move_right = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    maincharacter.move_left = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    maincharacter.move_left = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    maincharacter.shoot()

        maincharacter.output()
        pygame.display.flip()
        maincharacter.moving(screen)
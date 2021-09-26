#packages
import pygame
import time
import threading

game_statut = True



background_color = (200,200,200)

screen = pygame.display.set_mode((1024,512))

screen.fill(background_color)

pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
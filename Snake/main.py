#!/usr/bin/env python3

import pygame
from pygame.locals import *
import random
import time
import os
import turtle
from turtle import *
from pygame import *


if __name__ == "__main__":
    
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Snake")
    pygame.display.update()
    screen.fill((0, 0, 0))

    color_1 = (255, 255, 255) # white
    color_2 = (0, 0, 0) # black
    color_3 = (255, 0, 0) # red
    color_4 = (0, 255, 0) # green
    color_5 = (0, 0, 255) # yellow
    color_6 = (213, 200, 80) # yellow-green
    color_7 = (255, 255, 0) # orange

    # Snake

    timer = pygame.time.Clock()
    
    snake_body = 10
    snake_speed = 10

    def display_message(msg, color):

        font = pygame.font.SysFont("comicsansms", 25)
        text = font.render(msg, True, color)
        screen.blit(text, [screen.get_width() / 2 - text.get_width() / 2, screen.get_height() / 2 - text.get_height() / 2])

    def game_start():
        game_over = False
        game_close = False


    #Display_style = pygame.font.SysFont("comicsansms", 20)
    #score_font = pygame.font.SysFont("comicsansms", 40)
    

    def game_over(score):
        screen.fill((0, 0, 0))
        game_over_font = pygame.font.SysFont("comicsansms", 60)
        game_over_text = game_over_font.render("Game Over", True, color_3)
        screen.blit(game_over_text, (200, 250))
        pygame.display.update()
        time.sleep(3)
        quit()
    """
    game_loop = True

    while game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                game_loop = False

        screen.fill((0, 0, 0))
        pygame.display.update()
        time.sleep(0.1)
    snake_head = turtle.Turtle()
    """
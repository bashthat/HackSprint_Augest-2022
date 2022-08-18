#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
creating the snake game
"""

import pygame
import sys
import random
from pygame.locals import *
from pygame.math import Vector2


class Snake:

    def __init__(self):
        self.body = [Vector2(0, 0), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw(self):
        for blx in self.body:
            x_pos = int(blx.x * cell_size)
            y_pos = int(blx.y * cell_size)
            x_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen, (183, 191, 122), x_rect)

    def move(self):
        if self.new_length:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
            self.new_length = False
        else:

            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy

    def add_length(self):
        self.new_block = True


class FRUIT:

    def __init__(self):
        self.random_fruit()

    def spawn_fruit(self):
        fruit_obj = pygame.Rect(int(self.pos.x * cell_size, self.pos.y
                                * cell_size, cell_size, cell_size))
        pygame.draw.rect(screen, (255, 116, 155), fruit_obj)

    def random_fruit(self):
        self.x = random.randint(0, cell_num - 1)
        self.y = random.randint(0, cell_num - 1)
        self.position = Vector2(self.x, self.y)

    
    def move_snake(self):
        body_moves = self.body[:-1]
        body_moves.insert(0, self.body[0] + self.direction)
        self.body = body_moves[:]

class Game:

    def __init__(self):
        self.snake = Snake()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake[0]
        self.handle_events()

    def draw(self):
        self.snake.draw()
        self.fruit.spawn_fruit()

    def handle_events(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.random_fruit()
            self.snake.body.append(self.snake.body[-1]
                                   + self.snake.direction)
            print("fruit!")


pygame.init()
cell_size = 40
cell_num = 20
screen = pygame.display.set_mode((cell_num * cell_size, cell_num
                                 * cell_size))
clock = pygame.time.Clock()

fruit = FRUIT()
snake = Snake()

UPDATE_SCREEN = pygame.USEREVENT
pygame.time.set_timer(UPDATE_SCREEN, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == UPDATE_SCREEN:
            Game.update()
            snake.body_moves()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1, 0)

    screen.fill((170, 25, 200))
    fruit.draw_fruit()
    snake.draw()
    Game.draw()
    pygame.display.update()
    clock.tick(60)

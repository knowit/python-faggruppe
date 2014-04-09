#!/usr/bin/env python
"""
Skeleton provided to easily get started with pygame.
"""

import sys
import os
import collections

import pygame
from pygame import locals as const

BLACK = (0, 0, 0) # RGB
WHITE = (0xff, 0xff, 0xff)
WIDTH, HEIGHT = (1024, 768)
FPS = 60

Paddle = collections.namedtuple('Paddle', ['left_x', 'top_y', 'width', 'height'])
Ball = collections.namedtuple('Ball', ['center_x', 'center_y', 'radius', 'dx', 'dy'])
State = collections.namedtuple('State', ['left_player', 'right_player', 'ball'])

def main(argv):
    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('The name of the game')

    state = State(
        Paddle(WIDTH // 10, HEIGHT // 2, WIDTH // 50, HEIGHT // 20),
        Paddle(WIDTH - WIDTH // 10, HEIGHT // 2, WIDTH // 50, HEIGHT // 20),
        Ball(WIDTH // 2, HEIGHT // 2, 5, -5, 1)
    )

    while True:
        screen.fill(BLACK)

        pygame.draw.rect(screen, WHITE, state.left_player)
        pygame.draw.rect(screen, WHITE, state.right_player)
        pygame.draw.circle(screen, WHITE, (state.ball.center_x, state.ball.center_y), state.ball.radius, 0)

        for event in pygame.event.get():

            if event.type == const.QUIT:
                pygame.quit()
                return
            elif event.type == const.MOUSEMOTION:
                previous = state.left_player
                left_player = Paddle(previous.left_x, event.pos[1], previous.width, previous.height)
                state = State(left_player, state.right_player, state.ball)

        ball = state.ball
        next_tick = Ball(ball.center_x + ball.dx, ball.center_y + ball.dy, ball.radius, ball.dx, ball.dy)
        state = State(state.left_player, state.right_player, next_tick)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main(sys.argv[1:])

#!/usr/bin/env python3
# Forked from https://gist.github.com/bennuttall/6952575#gistcomment-2377898

import sys
from time import sleep
from random import randint
import pygame

DEBUG = True
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)


def createFullScreen(debug=DEBUG):
    """Create a fullscreen pygame screen."""

    # Get the available modes
    modes = pygame.display.list_modes(0)
    if debug:
        print(f"available resolutions: {modes}")

    # Recommended options for fullscreen
    options = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF

    # create the screen at default size with the options
    screen = pygame.display.set_mode((0, 0), options)
    pygame.display.set_caption("Conway's Game of Life")
    print("screen created, size is:", screen.get_size())
    return screen


def createWindowScreen(width=600, height=600, debug=DEBUG):
    """Create a windowed pygame screen."""

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Conway's Game of Life")
    print("screen created, size is:", screen.get_size())
    return screen

def pick_grid_size(screen):
    (xmax,ymax)= screen.get_size()
    return (xmax // 9, ymax // 9)

def make_empty_grid(x, y):
    grid = []
    for r in range(x):
        row = []
        for c in range(y):
            row.append(0)
        grid.append(row)
    return grid

def make_random_grid(x, y):
    grid = []
    points = 0
    for r in range(x):
        row = []
        for c in range(y):
            val = randint(0,1)
            points += val
            row.append(val)
        grid.append(row)
    print("Random world with %d points." % points)
    return grid

def evolve(grid):
    x = len(grid)
    y = len(grid[0])
    new_grid = make_empty_grid(x, y)
    for r in range(x):
        for c in range(y):
            cell = grid[r][c]
            neighbours = count_neighbours(grid, (r, c))
            new_grid[r][c] = 1 if evolve_cell(cell, neighbours) else 0
    return new_grid

def evolve_cell(alive, neighbours):
    return neighbours == 3 or (alive and neighbours == 2)

def count_neighbours(grid, position):
    x,y = position
    neighbour_cells = [(x - 1, y - 1), (x - 1, y + 0), (x - 1, y + 1),
                       (x + 0, y - 1),                 (x + 0, y + 1),
                       (x + 1, y - 1), (x + 1, y + 0), (x + 1, y + 1)]
    count = 0
    for x,y in neighbour_cells:
        if x >= 0 and y >= 0:
            try:
                count += grid[x][y]
            except:
                pass
    return count

def draw(screen, world):
    """Draw the current world."""
    screen.fill(WHITE)

    xlen = len(world)
    ylen = len(world[0])
    for x in range(xlen):
        for y in range(ylen):
            alive = world[x][y]
            cell_color = RED if alive else BLACK
            # print("x:%s y:%s color:%s" % (x, y, cell_color))
            draw_block(screen, x, y, cell_color)

def draw_block(screen, x, y, color):
    block_size = 9
    x *= block_size
    y *= block_size
    center_point = (x + (block_size // 2)), (y + (block_size // 2))
    pygame.draw.circle(screen, color, center_point, block_size // 2,0)

def main(debug=DEBUG):
    pygame.init()
    if debug:
        print("SDL version %s" % '.'.join(str(x) for x in pygame.get_sdl_version()))
    clock = pygame.time.Clock()
    screen = createFullScreen()

    grid_width, grid_height = pick_grid_size(screen)
    world = make_random_grid(grid_width, grid_height)

    exitRequest = False
    while not exitRequest:
        for event in pygame.event.get():
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(event.button==1): #left click
                    world = make_random_grid(grid_width, grid_height)
            if event.type == pygame.QUIT:
                exitRequest = True
            if event.type == pygame.KEYDOWN:
                exitRequest = True

        draw(screen, world)
        world = evolve(world)

        pygame.display.flip()
        clock.tick(15)
    pygame.quit()

if __name__ == "__main__":
    main()

import pygame
from Blockchain import Blockchain
import datetime
from enum import Enum

class Direction(Enum):
    continuer_tout_droit = 1
    faites_demi_tour = 2
    tourner_a_gauche = 3
    tourner_a_droite = 4

resolution = (600, 600)
screen = pygame.display.set_mode(resolution)
row, column = 20, 20
map_size = (row, column)  # (rows, columns)
line_width = 3
clock = pygame.time.Clock()  # to set max FPS

blockchain = Blockchain()

def evaluate_dimensions():
    # Evaluate the width and the height of the squares.
    square_width = (resolution[0] / map_size[0]) - line_width * ((map_size[0] + 1) / map_size[0])
    square_height = (resolution[1] / map_size[1]) - line_width * ((map_size[1] + 1) / map_size[1])
    return (square_width, square_height)

def convert_column_to_x(column, square_width):
    x = line_width * (column + 1) + square_width * column
    return x

def convert_row_to_y(row, square_height):
    y = line_width * (row + 1) + square_height * row
    return y

def draw_squares(car, blockchain):
    square_width, square_height = evaluate_dimensions()
    for row in range(map_size[0]):
        for column in range(map_size[1]):
            is_displayed = False
            if row == car.coords[1] and column == car.coords[0]:
              color = (220, 20, 60)  # (R, G, B)
              is_displayed = True
            else :
              for b in range(0, len(blockchain.chain)):
                if blockchain.chain[b].coords[0] == column and blockchain.chain[b].coords[1] == row:
                  color = (32, 178, 170)  # (R, G, B)
                  is_displayed = True
                  break
            if is_displayed == False:
              color = (100, 100, 100)
            x = convert_column_to_x(column, square_width)
            y = convert_row_to_y(row, square_height)
            geometry = (x, y, square_width, square_height)
            pygame.draw.rect(screen, color, geometry)

while True:
    clock.tick(60)  # max FPS = 60
    screen.fill((0, 0, 0))  # Fill screen with black color.
    draw_squares(blockchain.last_block, blockchain)
    pygame.display.flip()  # Update the screen.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            blockchain.display_blockchain()
            pygame.quit()
            quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                data_direction = Direction.continuer_tout_droit.name
                deplacement = [0,-1]
                time_changement = datetime.datetime.now().strftime('%A, %Y-%m-%d %Hh:%Mm:%Ss')
                data = data_direction + ' - ' + time_changement
                blockchain.create_block_in_chain(data, deplacement, row, column)
                
          
            if event.key == pygame.K_s:
                data_direction = Direction.faites_demi_tour.name
                deplacement = [0,1]
                time_changement = datetime.datetime.now().strftime('%A, %Y-%m-%d %Hh:%Mm:%Ss')
                data = data_direction + ' - ' + time_changement
                blockchain.create_block_in_chain(data, deplacement, row, column)
        
            if event.key == pygame.K_q:
                data_direction = Direction.tourner_a_gauche.name
                deplacement = [-1,0]
                time_changement = datetime.datetime.now().strftime('%A, %Y-%m-%d %Hh:%Mm:%Ss')
                data = data_direction + ' - ' + time_changement
                blockchain.create_block_in_chain(data, deplacement, row, column)
        
            if event.key == pygame.K_d:
                data_direction = Direction.tourner_a_droite.name
                deplacement = [1,0]
                time_changement = datetime.datetime.now().strftime('%A, %Y-%m-%d %Hh:%Mm:%Ss')
                data = data_direction + ' - ' + time_changement
                blockchain.create_block_in_chain(data, deplacement, row, column)
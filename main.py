from Blockchain import Blockchain
from Map import Map
import datetime
from enum import Enum

class Direction(Enum):
    continuer_tout_droit = 1
    faites_demi_tour = 2
    tourner_a_gauche = 3
    tourner_a_droite = 4
    
blockchain = Blockchain()

new_york_city = Map(20, 20)

game_direction = True
    
while game_direction:
    
    print("Press z to go forward, s to go back, d to turn right, q to go left or a to quit")
    variable = input('Please enter your choice : ')
    
    if variable == "z":
        data_direction = Direction.continuer_tout_droit.name
        deplacement = [0,-1]
    elif variable == "s":
        data_direction = Direction.faites_demi_tour.name
        deplacement = [0,1]
    elif variable == "d":
        data_direction = Direction.tourner_a_droite.name
        deplacement = [1,0]
    elif variable == "q":
        data_direction = Direction.tourner_a_gauche.name
        deplacement = [-1,0]
    elif variable == "a":
        game_direction = False
        
    time_changement = datetime.datetime.utcnow().strftime('%Y-%m-%d %Hh:%Mm:%Ss')

    data = data_direction + ' - ' + time_changement

    blockchain.create_block_in_chain(data, deplacement, new_york_city.length, new_york_city.height)

    blockchain.display_blockchain()
    
    new_york_city.display_map(blockchain.last_block, blockchain)
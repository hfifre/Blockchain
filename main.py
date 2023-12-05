from Blockchain import Blockchain
from Data import *

blockchain = Blockchain()

game_direction = True


while game_direction:
    
    print("Press z to go forward, s to go back, d to turn right, q to go left or a to quit")
    variable = input('Please enter your choice : ')
    
    if variable == "z":
        data_direction = Donnee(Direction.continuer_tout_droit.name).direction 
    elif variable == "s":
        data_direction = Donnee(Direction.faites_demi_tour.name).direction 
    elif variable == "d":
        data_direction = Donnee(Direction.tourner_a_droite.name).direction 
    elif variable == "q":
        data_direction = Donnee(Direction.tourner_a_gauche.name).direction 
    elif variable == "a":
        game_direction = False
        
    time_changement = datetime.datetime.utcnow().strftime('%Y-%m-%d %Hh:%Mm:%Ss')

    data = data_direction + ' - ' + time_changement

    blockchain.create_block_in_chain(data)

    blockchain.display_blockchain()
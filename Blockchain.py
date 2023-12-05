from Block import Block
import datetime

class Blockchain:
  
  def __init__(self):
    self.chain = []
    self.generate_first_block()

  def generate_first_block(self):
    self.chain.append(Block("first_block", "1", datetime.datetime.utcnow, [0, 0]))
  
  def create_block_in_chain(self, data, deplacement, length, height):
    previous_block_hash = self.last_block.block_hash
    coordonnees = [0, 0]
    coordonnees[0] = self.last_block.coords[0] + deplacement[0]
    coordonnees[1] = self.last_block.coords[1] + deplacement[1]
    if coordonnees[0] < length and coordonnees[0] >= 0 \
    and coordonnees[1] < height and coordonnees[1] >= 0:
        self.chain.append(Block(data,previous_block_hash, datetime.datetime.utcnow, coordonnees))
  
  def display_blockchain(self):
    for i in range(len(self.chain)):
      print(f"Data {i + 1}: {self.chain[i].data} - {self.chain[i].coords}")
      print(f"Hash {i + 1}: {self.chain[i].block_hash}\n------")
  
  @property
  def last_block(self):
    return self.chain[-1]
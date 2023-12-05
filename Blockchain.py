from Block import Block

class Blockchain:
  
  def __init__(self):
    self.chain = []
    self.generate_first_block()

  def generate_first_block(self):
    self.chain.append(Block("first_block", "0"))
  
  def create_block_in_chain(self, data):
    previous_block_hash = self.last_block.block_hash
    self.chain.append(Block(data,previous_block_hash))
  
  def display_blockchain(self):
    for i in range(len(self.chain)):
      print(f"Data {i + 1}: {self.chain[i].data}")
      print(f"Hash {i + 1}: {self.chain[i].block_hash}\n------")
  
  @property
  def last_block(self):
    return self.chain[-1]
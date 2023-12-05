import hashlib

class Block:
  
  def __init__(self, data, previous_hash, datetime):
    self.data = data
    self.previous_hash = previous_hash
    self.block_hash = hashlib.sha256(self.data.encode()).hexdigest()
    self.datetime = datetime
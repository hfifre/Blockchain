import hashlib

class Block:
  
  def __init__(self, data, previous_hash, datetime, coords):
    self.data = data
    self.previous_hash = previous_hash
    self.datetime = str(datetime)
    self.coords = coords
    self.block_hash = hashlib.sha256(self.data.encode() + self.previous_hash.encode() + self.datetime.encode()).hexdigest()
    
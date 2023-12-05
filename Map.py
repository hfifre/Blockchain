class Map:
  
  def __init__(self, length, height):
    self.length = length
    self.height = height
    self.board = [[]]
    for i in range(0, height):
      line = []
      for j in range(0, length):
        line.append([])
      self.board.append(line)
  
  def display_map(self, car, blockchain):
    for i in range(0, self.height):
      print("|", end="")
      for j in range(0, self.length):
        is_displayed = False
        if i == car.coords[1] and j == car.coords[0]:
          print("[X]", end="")
          is_displayed = True
        else :
            for b in range(0, len(blockchain.chain)):
              if blockchain.chain[b].coords[0] == j and blockchain.chain[b].coords[1] == i:
                print("[*]", end="")
                is_displayed = True
                break;
        if is_displayed == False:
          print("[ ]", end="")
      print("|")


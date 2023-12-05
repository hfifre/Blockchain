class Map:
  
  def __init__(self, length, height):
    self.length = length
    self.height = height
    self.board = [[]]
    for i in range(1, height+1):
      line = []
      for j in range(0, length):
        line.append({"x" : j, "y" : i, "has_car" : False})
      self.board.append(line)
    self.board[1][1]["has_car"] = True
  
  def display_map(self):
    for i in range(1, self.height):
      print("|", end="")
      for j in range(1, self.length):
        if(self.board[i][j]["has_car"]):
          print(f"[X]", end="")
        else:
          print(f"[ ]", end="")
      print("|")
  
  def search_car(self):
    for i in range(1, self.height):
      for j in range(1, self.length):
        if self.board[i][j]["has_car"]:
          return self.board[i][j]
  
  def move_car(self, x_value, y_value):
    car = self.search_car()
    
    if car["x"] + x_value >= self.length or car["x"] + x_value <= 0 \
    or car["y"] + y_value >= self.height or car["y"] + y_value <= 0:
      print("can't go out of the map")
      return
    
    self.board[car["y"]][car["x"]]["has_car"] = False
    self.board[car["y"]+y_value][car["x"]+x_value]["has_car"] = True


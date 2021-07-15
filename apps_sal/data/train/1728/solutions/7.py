class PlayerMovement:
    def __init__(self, x, y):
        self.position = Tile(x, y)
        self.direction = 8
        self.pressed = []
        self.movements = {8: (0, 1), 2: (0, -1), 6: (1, 0), 4: (-1, 0)}

    def update(self):
        newkey = False
        if any(Input.get_state(x) for x in (2, 4, 6, 8)):
            if Input.get_state(6):
                if not 6 in self.pressed:
                    self.pressed.append(6)
                    self.direction = 6
                    newkey = True
            else:
                if 6 in self.pressed:
                    if self.pressed[-1] == 6:
                        newkey = True
                        if len(self.pressed) > 1:
                            self.direction = self.pressed[-2]
                    self.pressed.remove(6)
    
            if Input.get_state(4):
                if not 4 in self.pressed:
                    self.pressed.append(4)
                    self.direction = 4
                    newkey = True
            else:
                if 4 in self.pressed:
                    if self.pressed[-1] == 4:
                        newkey = True
                        if len(self.pressed) > 1:
                            self.direction = self.pressed[-2]
                    self.pressed.remove(4)
            
            if Input.get_state(2):
                if not 2 in self.pressed:
                    self.pressed.append(2)
                    self.direction = 2
                    newkey = True
            else:
                if 2 in self.pressed:
                    if self.pressed[-1] == 2:
                        newkey = True
                        if len(self.pressed) > 1:
                            self.direction = self.pressed[-2]
                    self.pressed.remove(2)
            
            if Input.get_state(8):
                if not 8 in self.pressed:
                    self.pressed.append(8)
                    self.direction = 8
                    newkey = True
            else:
                if 8 in self.pressed:
                    if self.pressed[-1] == 8:
                        newkey = True
                        if len(self.pressed) > 1:
                            self.direction = self.pressed[-2]
                    self.pressed.remove(8)
                    
        else:
            self.pressed = []
            newkey = True
        
        if not newkey and self.pressed:
            self.position = Tile(self.position.x + self.movements[self.direction][0], self.position.y + self.movements[self.direction][1])


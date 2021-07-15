from collections import Counter
class PlayerMovement:

    def __init__(self, x, y):
        self.position = Tile(x, y)
        self.direction = 8
        self.moves = {8:[0,1],2:[0,-1],4:[-1,0],6:[1,0]}
        self.keys = []
    def update(self):
        release = [i for i in [8,2,4,6] if not Input.get_state(i)]
        if any(i in self.keys for i in release):
            if len(self.keys)==1 : return self.keys.pop()
            for i in release:
                if i in self.keys : self.keys.pop(len(self.keys)-self.keys[::-1].index(i)-1)
            if not self.keys : return
            if self.direction == self.keys[-1]:
                  inc,dec = self.moves[self.direction]
                  self.position = Tile(self.position.x+inc,self.position.y+dec)
            self.direction = self.keys[-1]
        else:
            direction = [i for i in [8,2,4,6] if Input.get_state(i)]
            new, c = list((Counter(direction)-Counter(self.keys)).elements()), bool(self.keys)
            if not new and not self.keys : return
            self.keys.extend(sorted(new,key=[6,4,2,8].index))
            d = self.keys[-1]
            if not c or (d != self.direction): self.direction = d ; return
            inc,dec = self.moves[self.direction]
            self.position = Tile(self.position.x+inc,self.position.y+dec)

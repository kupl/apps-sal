class PlayerMovement:                                              # class by MMMAAANNN @ codewars.com

    KEYS = 6, 4, 2, 8                                              # In order of reverse priority
    DIRS = dict(list(zip(KEYS, (( 1,  0),                               # Associating with directions
                           (-1,  0),
                           ( 0, -1),
                           ( 0,  1)))))
    
    def __init__(self, x, y):
        self.position  = Tile(x, y)
        self.direction = 8
        self.previous  = {i: False for i in self.KEYS}            # Event detection
        self.keystack  = [0]                                      # The order of keypress

    def update(self):
        current = dict(list(Input.STATES.items()))                      # Read current state
        if (current != self.previous):                            # Skip recalc if no events happened
            change = {i : current[i] - self.previous[i]           # Calculate type of change
                      for i in self.KEYS}
            for key in self.KEYS:                                 # Update the status of keystack
                if   change[key] > 0:
                    self.keystack.append(key)
                elif change[key] < 0:
                    self.keystack.remove(key)
        if (self.keystack[-1] == self.direction                   # Movement only if no turn required
            and sum(self.previous.values())):                     # Avoid moving if first event after idle
            dx, dy = self.DIRS[self.direction]                    # Reading the movement vector
            self.position = Tile(self.position.x + dx,            # Updating coordinates: x
                                 self.position.y + dy)            #               ... and y
        else:
            self.direction = self.keystack[-1] or self.direction  # Turning if needed
        self.previous = current                                   # Remember state to detect next event


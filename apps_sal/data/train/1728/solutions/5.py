class PlayerMovement:
    
    PREC   = [8,        2,         4,        6]                                                                               # Order of precedence
    I_KEYS = {8: 0,     2: 1,      4: 2,      6: 3}                                                                           # Index of the keys in self.pressed
    MOVES  = {8: (0,1), 2: (0,-1), 4: (-1,0), 6: (1,0)}                                                                       # Moves directions

    def __init__(self, x, y):
        self.position  = Tile(x, y)                                                                                           # Current position
        self.direction = 8                                                                                                    # Current direction of move
        self.pressed   = [0,0,0,0]                                                                                            # Keys currently pressed or not (True/False)
        self.stack     = []                                                                                                   # Stack representing the order of the pressed keys (according to pressing order AND precedence if multiple pressing at the same time)

    def update(self):
        state       = [Input.get_state(d) for d in self.PREC]                                                                 # State of the art at update time
        
        newPressed  =     [ d for i,d in enumerate(self.PREC) if not self.pressed[i] and state[i] ]                           # All keys freshly pressed
        notReleased = next((d for d   in self.stack[::-1]  if self.pressed[self.I_KEYS[d]] and state[self.I_KEYS[d]]), None)  # Last key that has not been released yet (according to the order of the stack[::-1] because one search for the last pressed)
        releasedLst =     [ d for i,d in enumerate(self.PREC) if self.pressed[i] and not state[i] ]                           # All keys freshly released
        
        if newPressed:                                                                                                        # If new key pressed:
            self.direction = newPressed[0]                                                                                    #     Update direction with higher precedence
            for t in newPressed[::-1]: self.stack.append(t)                                                                   #     append all the new kleys to the stack, lower preccedence first
            
        elif self.direction in releasedLst:                                                                                   # If the current direction has been released:
            self.direction = notReleased or self.direction                                                                    #     upadte direction. If no pressed key remain, do not update
                
        elif notReleased:                                                                                                     # If current direction still pressed and no other key pressed in the meantime:
            self.position  = Tile(*( z+dz for z,dz in zip([self.position.x, self.position.y], self.MOVES[notReleased]) ))     #     MOVE!
            
        self.pressed = state                                                                                                  # Archive current state of keys
        for t in releasedLst: self.stack.remove(t)                                        

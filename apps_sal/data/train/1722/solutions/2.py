class Machine:

    def __init__(self):
        self.actptr = 0
    
    def command(self, cmd, num):
        return ACTIONS()[(cmd + self.actptr) % 5](num)
        
    def response(self,res):
        if not res: self.actptr += 1


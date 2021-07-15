class TvRemote():
    def __init__(self,words):
        self.x, self.y = (0, 0)
        self.presses = 0
        self.mode = 1
        self.modes = ["",
                      "abcde123fghij456klmno789pqrst.@0uvwxyz_/æ øøøøøø", 
                      "ABCDE123FGHIJ456KLMNO789PQRST.@0UVWXYZ_/æ øøøøøø",
                    """^~?!'"()-:;+&%*=<>€£$¥¤\[]{},.@§#¿¡øøø_/æ øøøøøø"""]
    
        words = words.replace("\u00a1","¡")
        words = words.replace("\u00a3","£")
        words = words.replace("\u00a4","¤")
        words = words.replace("\u00a5","¥")
        words = words.replace("\u00a7","€")
        words = words.replace("\u00bf","¿")
        words = words.replace("\u20ac","€")
        self.words = words
        print(words)
    
    def buttonPresses(self):
        for letter in self.words:
            self.presses += self.taxiCabDist(letter)
            print(self.presses,"\n")
            
        return self.presses
    
    
    def switchMode(self):
        print("EEROROROROROROR")
        self.mode += 1
        if self.mode > 3:
            self.mode = 1
            
        return self.taxiCabDist("æ")
    
    def taxiCabDist(self,letter):
        #SwitchMode
        modeSwitch = 0
        if letter not in self.modes[self.mode]:
            modeSwitch += self.switchMode()
            if letter not in self.modes[self.mode]:
                modeSwitch += self.switchMode()
                
        #Letter coord 
        index = self.modes[self.mode].index(letter)
        x, y = index % 8, index // 8
        
        #Absolute difference coord
        dx = abs(self.x-x)
        dy = abs(self.y-y)
        
        #log
        print(letter,(dx,dy),dx + dy + modeSwitch + 1)
        
        #Set New Cursor Position
        self.x = x
        self.y = y
        
        return dx + dy + modeSwitch + 1 # The OK Press
    
def tv_remote(word):
    return TvRemote(word).buttonPresses()

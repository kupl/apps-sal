class Word:
    
    def __init__(self,string=None):
        self.string = string
    
    def isup(self,string):
        if ord(string)-96 > 0:
            if not string.isalpha():
                return True 
            return False
        return True
        
    def is_upper(self):
        string = self.string
        for i in range(len(string)):
            if not (self.isup(string[i])):
                return False
        return True
        


def is_uppercase(string):
    a = Word(string)
    return a.is_upper()


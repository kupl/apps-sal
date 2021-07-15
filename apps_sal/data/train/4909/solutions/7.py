from datetime import datetime
class Random():
    def __init__(self, seed):
        self.seed=seed
        self.x=self.next_x(self.seed)
    
    @property
    def seed(self):
        return self.__seed

    @seed.setter
    def seed(self,seed):
        self.x=self.next_x(seed)
        self.__seed=seed
    
    def next_x(self,x):
        x=x^(x<<13&0xFFFFFFFF)
        x=x^(x>>17&0xFFFFFFFF)
        x=x^(x<<15&0xFFFFFFFF)
        return x&0xFFFFFFFF
    
    def random(self):
        x=self.x
        self.x=self.next_x(x)
        return x/(2**32)
        
    def randint(self, start, end):
        x=self.x
        self.x=self.next_x(x)
        return (end-start)*x//(2**32)+start

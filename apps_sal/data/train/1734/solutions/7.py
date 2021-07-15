class User():
    def __init__(self):
        self.rank = -8
        self.ranks = [-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]
        self.relative_rank = self.ranks.index(self.rank)
        self.progress = 0
        
    
    def rank(self):
        print("rank")
        print((self.rank))
        print((self.progress))
        return self.rank
    def progress(self):
        print("progrees")
        print((self.rank))
        print((self.progress))
        return self.progress
    
    
    def inc_progress(self,kata):
        print("inc:")
        print(("rank",self.rank))
        print(("rank relative",self.relative_rank))
        print(("progress",self.progress))
        print(("kata",kata))
        
        if kata > 8 or kata < -8 or kata == 0:
            raise "Bruh"
        
        relative_rank = self.ranks.index(kata) ### Relvative rank of the kata. Starts from 0, goes to 15.
        print(("kata relative",relative_rank))
        
        print()
        if self.rank == kata:
            self.progress += 3
        elif self.relative_rank - 1 == relative_rank and self.relative_rank != 0:
            self.progress += 1
        elif self.relative_rank < relative_rank:
            self.progress += 10 * ((relative_rank - self.relative_rank) ** 2)
        
        if self.progress >= 100:
            self.relative_rank += self.progress // 100
            if self.relative_rank > 15:
                self.relative_rank = 15
    
            self.progress %= 100
        
            self.rank = self.ranks[self.relative_rank]
        if self.rank > 7:
            self.progress = 0
            


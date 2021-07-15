class StreamChecker:

    def __init__(self, words: List[str]):
        
        self.s = ''
        self.c = 0
       
        self.ld = dict()
        self.lths = set()
        
        for x in list(set(words)):
            lim = len(x)
            self.lths.add(lim)
            try:
                self.ld[lim][x[-1]].add(x)
            except:
                try:
                    self.ld[lim][x[-1]]=set()
                    self.ld[lim][x[-1]].add(x)
                except:
                    self.ld[lim]=dict()
                    self.ld[lim][x[-1]]=set()
                    self.ld[lim][x[-1]].add(x)
                    
         
        
    def query(self, letter: str) -> bool:
        self.s+=letter
        self.c+=1
        ###print(self.s,self.c)
        
        for y in self.lths:
            
            if y<=self.c:
                ###print(self.s[-y:])
                if self.s[-1] in self.ld[y]:
                    if self.s[-y:] in self.ld[y][self.s[-1]]:

                        return True
                
        
        return False
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


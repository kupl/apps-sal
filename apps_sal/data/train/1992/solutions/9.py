from queue import Queue
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        
        self.characters=characters
        self.combinationLength=combinationLength
        self.arr=[0]*26
        for i in self.characters:
            temp=ord(i)
         
            self.arr[temp-97]+=1
            
        
        self.q=Queue(maxsize=10001)
        self.solve(self.arr,self.combinationLength,self.q,0,\"\")
        
        
        
    
    
    def solve(self,arr,sizee,bag,ind,cur):
        if(len(cur)==sizee):
            bag.put(cur)
            return bag
        
        
        for i in range(ind,26):
            if(arr[i]!=0):
                arr[i]-=1
                bag=self.solve(arr,sizee,bag,i,cur+chr(i+97))
            
                arr[i]+=1
        
        return bag
                
                
                
                
        

    def next(self) -> str:
        
        return self.q.get()

    def hasNext(self) -> bool:
        return not self.q.empty()
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

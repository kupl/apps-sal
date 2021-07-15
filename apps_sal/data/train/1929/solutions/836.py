

    
class StreamChecker:

    
    def __init__(self, words: List[str]):
        self.Trie={'chld':{},'end':False}
        
        for word in words:
            T=self.Trie
            for l in reversed(word):
                if l not in T['chld']:
                    T['chld'][l]={'chld':{},'end':False}
                T=T['chld'][l]
                
            T['end']=True
            
        self.stack=''
        
        

    def query(self, letter: str) -> bool:
        
        self.stack+=letter
        
        T=self.Trie
        for i in range(len(self.stack)-1,-1,-1):
            l=self.stack[i]
            if l not in T['chld']:
                #print (letter)
                return False
            T=T['chld'][l]
            if T['end']:
               # print(l,letter)
                return True
        
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


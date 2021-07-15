class StreamChecker:

    def __init__(self, words: List[str]):
        
        self.d = {}
        
        for word in words:
            ptr = self.d
            for c in word:
                if c not in ptr:
                    ptr[c] = {}
                ptr = ptr[c]
            ptr[''] = True 
                
        self.curr = self.d
        self.q = []
        

    def query(self, letter: str) -> bool:

        self.q.append(self.d)
        
        # print(letter, len(self.q))
        temp = []
        flag = False
        for ptr in self.q:            
            if letter in ptr:
                ptr = ptr[letter]
                temp.append(ptr)
                if '' in ptr:
                    flag = True
        
        self.q = temp
        
        return flag
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


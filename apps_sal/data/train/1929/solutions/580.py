class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie={}
        for i in words:
            k=self.trie
            j=i[::-1]
            for f in j:
                if f not in k:
                    k[f]={}
                k=k[f]
            k['$']=1
        print(self.trie)
        self.past=\"\"

    def query(self, letter: str) -> bool:
        self.past+=letter
        ans=True
        k=self.trie
        for i in self.past[::-1]:
            if i not in k:
                ans=False
                break
            k=k[i]
            if '$' in k:
                break
        if ans and '$' in k:
            return True
        return False
                
            
            
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

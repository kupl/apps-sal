class StreamChecker:

    def __init__(self, words: List[str]):
        self.chars=[]
        self.trie={}
        for word in words:
            curr=self.trie
            for c in reversed(word):
                if c not in curr:
                    curr[c]={}
                curr=curr[c]
            curr['#']=True
    
    def search(self):
        ind=len(self.chars)-1
        curr=self.trie
        while curr and ind>=0:
            if '#' in curr:
                return True
            c=self.chars[ind]
            if c not in curr:
                return False
            
            curr=curr[c]
            ind-=1
        return curr and '#' in curr
        

    def query(self, letter: str) -> bool:
        self.chars.append(letter)
        return self.search()


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


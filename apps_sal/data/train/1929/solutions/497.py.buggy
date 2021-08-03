class node:
    def __init__(self):
        self.child=[None]*26
        self.end=False
class trie:
    def __init__(self):
        self.q=node()
    def insert(self,sen):
        sen=sen[::-1]
        p=self.q
        for x in sen:
            if p.child[ord(x)-ord('a')]==None:
                p.child[ord(x)-ord('a')]=node() 
            p=p.child[ord(x)-ord('a')]
        p.end=True
class StreamChecker:
   
    def __init__(self, words: List[str]):
        self.p1=trie()
        self.s=\"\"
        for x in words:
            self.p1.insert(x)
            
    def query(self, letter: str) -> bool:
        self.s+=letter
        root=self.p1.q
        #ind=ord(letter)-ord('a')
        for x in self.s[::-1]:
            ind=ord(x)-ord('a')
            root=root.child[ind]
            if root!=None:
                if root.end==True: 
                    return True
            else:
                break

        return False 
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

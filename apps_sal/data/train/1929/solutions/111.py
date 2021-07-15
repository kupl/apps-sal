# Written with love by atm1504
class TrieNode:
    def __init__(self):
        self.children={}
        self.isWord=False
class StreamChecker:
    def __init__(self, words: List[str]):
        self.root=TrieNode()
        self.letters=\"\"
        
        for word in words:
            self.insertWord(word)
        
    def insertWord(self,word):
        node=self.root
        word=word[::-1]
        for x in word:
            if x not in node.children:
                node.children[x]=TrieNode()
            node=node.children[x]
        node.isWord=True
        
    def query(self, letter: str) -> bool:
        self.letters+=letter
        k=0
        n=len(self.letters)
        node=self.root
        for i in range(n-1,-1,-1):
            x=self.letters[i]
            k+=1
            if x not in node.children:
                return False
            node=node.children[x]
            if k>0 and node.isWord:
                return True
        return False

class TreeNode:
    def __init__(self,chr):
        self.val = chr
        self.children = {}
        self.leaf = False



class StreamChecker:

    def __init__(self, words: List[str]):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.root = TreeNode(None)
        for word in words:
            self.insert(''.join(reversed(word)))
        self.ans=''

    def insert(self, word: str) -> None:
        \"\"\"
        Inserts a word into the trie.
        \"\"\"
        parent = self.root
        for c in word:
            if(c not in parent.children):
                parent.children[c] = TreeNode(c)
            parent = parent.children[c]
        parent.leaf = True
        

    def search(self, word: str) -> bool:
        \"\"\"
        Returns if the word is in the trie.
        \"\"\"
        parent = self.root
        for c in word:
            if(c not in parent.children):
                return False
            parent = parent.children[c]
            if(parent.leaf):
                return True
        return False
                
          

    def query(self, letter: str) -> bool:
        self.ans=letter+self.ans
        return self.search(self.ans)
        
            
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

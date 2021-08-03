class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
    def insert(self, word):
        if len(word)==0:
            self.isEnd = True
            return
        if word[0] not in self.children:
            self.children[word[0]] = Trie()
        self.children[word[0]].insert(word[1:])
        
    def search(self, word):
        if len(word)==0:
            return (True, False)
        if len(word)==1:
            return (word[0] in self.children, word[0] in self.children and self.children[word[0]].isEnd)
        startsWith = word[0] in self.children
        if startsWith:
            return self.children[word[0]].search(word[1:])

        return (False, False)

    def startsWith(self, word):
        if len(word)==0:
            return True
        return word[0] in self.children and self.children[word[0]].startsWith(word[1:])
    def next(self, char):
        if char in self.children:
            return self.children[char]
        return None
    def printNode(self):
        print(self.children,self.isEnd)

class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = Trie()
        for word in words:
            self.words.insert(word[::-1])
        self.stream = \"\"

    def query(self, letter: str) -> bool:
        self.stream += letter
        node = self.words
        for i in range(len(self.stream)-1, -1, -1):
            node = node.next(self.stream[i])
            if node==None:
                return False
            if node.isEnd:
                return True
            
                
        return False
    
                
                
                
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

class Trie:
    def __init__(self):
        self.childern = defaultdict(Trie)
        self.end = False
        
class StreamChecker:
    def __init__(self, words: List[str]):
        self.inTrie = Trie()
        self.querystr = \"\"
        for word in words:
            self.addWord(word[::-1])
                
    def addWord(self, word):
        node = self.inTrie
        for symbol in word:
            node = node.childern[symbol]
        node.end = True
    
    def search(self, node, word):
        if not word:
            return node.end == True
        if node.end:
            return True
        node = node.childern.get(word[0])
        if not node:
            return False
        return self.search(node, word[1:])
        
    def query(self, letter: str) -> bool:
        self.querystr = letter + self.querystr
        return self.search(self.inTrie, self.querystr)
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

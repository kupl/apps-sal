class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False
        self.word = \"\"
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = \"\"
        self.root = TrieNode()
        self.maxL = 0
        for word in words:
            self.maxL = max(self.maxL, len(word))
            self.add(word)
    
    def add(self, word):
        p = self.root
        for c in word[::-1]:
            idx = ord(c) - ord('a')
            if not p.children[idx]:
                p.children[idx] = TrieNode()
            p = p.children[idx]
        p.isEnd = True
        p.word = word
        

    def query(self, letter: str) -> bool:
        if len(self.stream) < self.maxL:
            self.stream = letter + self.stream   # ba
        else:
            self.stream = self.stream[:-1]
            self.stream = letter + self.stream 
      
        p = self.root 
        for c in self.stream:
            idx = ord(c) - ord('a')
            if not p.children[idx]:
                return False
            if p.children[idx].isEnd:
                return True
            p = p.children[idx]
    
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

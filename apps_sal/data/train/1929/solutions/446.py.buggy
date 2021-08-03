class Trie:
    def __init__(self, c: str = None):
        self.c = c
        self.ch = [None] * 26
        self.isEnd = False
    
    def insert(self, word: List[str], idx: int = None):
        # print(\"start\", self)
        if idx is None:
            idx = len(word) - 1        
        if idx == -1:
            self.isEnd = True
            # print(\"insert to end\", self)            
            return
        c = ord(word[idx]) - ord('a')
        if self.ch[c] is None:
            self.ch[c] = Trie(word[idx])
        self.ch[c].insert(word, idx-1)
        # print(self)        
    
    def __str__(self):
        out = []
        for i in range(26):
            if self.ch[i] is None:
                continue
            out.append(chr(i + ord('a')) + \"{%r}\"%(str(self.ch[i])))
        return \"[%r,%r] \"%(self.c, self.isEnd) + \" \".join(out)
            
        
    def query(self, word: List[str], idx: int = None):
        if self.isEnd:
            return True
        if idx is None:
            idx = len(word) - 1
        if idx == -1:
            return self.isEnd
        c = ord(word[idx]) - ord('a')
        if self.ch[c] is None:
            return False
        return self.ch[c].query(word, idx-1)
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Trie(\"*\")
        maxLen = 0
        for w in words:
            wli = [c for c in w]
            self.root.insert(wli)
            maxLen = max(maxLen, len(wli))
        self.maxLen = maxLen
        self.buf = []
        # print(\"final \", str(self.root))

    def query(self, letter: str) -> bool:
        self.buf.append(letter)
        return self.root.query(self.buf)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

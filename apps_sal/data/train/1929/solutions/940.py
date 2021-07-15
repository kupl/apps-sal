class Trie:
    
    def __init__(self):
        self.root = dict()
        self.ptr = []
        
    def add(self, word):
        curr = self.root
        for c in word:
            if not c in curr:
                curr[c] = dict()
            curr = curr[c]
        
        curr['$'] = dict()
        
    def search(self, c):
        self.ptr.append(self.root)
        new_ptr = []
        ans = False
        for ptr in self.ptr:
            if c in ptr:
                new_ptr.append(ptr[c])
        self.ptr = new_ptr
        
        return any(['$' in p for p in self.ptr])
    
class StreamChecker:

    def __init__(self, words: List[str]):
        self.T = Trie()
        for word in words:
            self.T.add(word)

    def query(self, letter: str) -> bool:
        return self.T.search(letter)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


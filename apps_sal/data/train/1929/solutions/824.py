class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            root = self.trie
            for w in word:
                if w not in root:
                    root[w] = {}
                root = root[w]
            root['#'] = {}
        self.q = []
            
        

    def query(self, letter: str) -> bool:
        i = 0
        self.q = [p[letter] for p in self.q if letter in p]
        if letter in self.trie:
            self.q.append(self.trie[letter])
        for p in self.q:
            if '#' in p:
                return True
        return False
            

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


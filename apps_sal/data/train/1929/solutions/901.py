class StreamChecker:

    def __init__(self, words: List[str]):
        Trie = lambda: defaultdict(Trie)
        self.root = Trie()
        self.end = True
        self.words = words
        self.prevs = []
        
        for i, word in enumerate (words):
            reduce (dict.__getitem__, word, self.root)[self.end] = i
        

    def query(self, letter: str) -> bool:
        result = False
        self.prevs.append(self.root)
        if self.prevs:
            new_prevs = []
            for prev in self.prevs:
                if letter in prev:
                    new_prevs.append(prev[letter])
                    result = result or self.end in new_prevs[-1]
            self.prevs = new_prevs
        return result
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


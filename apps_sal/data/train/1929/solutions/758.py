class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = self._trie()
        self._fillTrie(words)
        self.q = []
        
    def _trie(self):
        return defaultdict(self._trie)
    
    def _fillTrie(self, words):
        for w in words:
            t = self.trie
            for c in w:
                t = t[c]
            t['*']
            
    def query(self, letter: str) -> bool:
        found,newQ = False,[]
        self.q.append(self.trie)
        
        for t in self.q:
            if letter in t:
                t = t[letter]
                newQ.append(t)
                found |= '*' in t
        self.q = newQ
        return found
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.hist = \"\"
        
        for word in words:
            t = self.trie
            for w in word[::-1]:
                if w not in t:
                    t[w] = {}
                t = t[w]
            t['$'] = '$'

    def query(self, letter: str) -> bool:
        self.hist += letter
        ctrie = self.trie
        for l in self.hist[::-1]:
            if l not in ctrie:
                return False
            ctrie = ctrie[l]
            
            if '$' in ctrie:
                return True
        return False
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

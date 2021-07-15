class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = self.create_trie(words)
        self.l = []

    def create_trie(self, words):
        trie = {}
        for word in words:
            curr = trie
            for ch in word:
                if ch not in curr:
                    curr[ch] = {}
                curr = curr[ch]
            curr['.'] = True
        return trie
            
        
    def query(self, letter: str) -> bool:
        self.l.append(self.trie)
        self.l = [trie[letter] for trie in self.l if letter in trie]
        return any('.' in trie for trie in self.l)
                
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = dict()
        for word in words:
            d = self.trie
            for char in word:
                if char not in d:
                    d[char] = dict()
                d = d[char]
            d['*'] = False            
                
        self.recent = list()
        

    def query(self, letter: str) -> bool:
        self.recent = [d[letter] for d in self.recent if letter in d]
        if letter in self.trie:
            self.recent.append(self.trie[letter])
        return any('*' in d for d in self.recent)
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


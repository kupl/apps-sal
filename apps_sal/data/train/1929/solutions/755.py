class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            cur = self.trie
            for char in word:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur['~'] = word
            
        self.candidates = []

    def query(self, letter: str) -> bool:
        newCands = []
        foundWord = False
        
        if letter in self.trie:
            newCands.append(self.trie[letter])
            if '~' in self.trie[letter]:
                foundWord = True
                
        for cand in self.candidates:
            if letter in cand:
                newCands.append(cand[letter])
                if '~' in cand[letter]:
                    foundWord = True
        
        self.candidates = newCands
        return foundWord


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


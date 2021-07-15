class StreamChecker:    
    def __init__(self, words: List[str]):
        self.data = {}
        for word in words:
            self._add_word(word)
        self.q = []
    
    def _add_word(self, word):
        word += '$'
        d = self.data
        for char in word:
            if char not in d:
                d[char] = {}
            d = d[char]

    def query(self, letter: str) -> bool:
        new_q = []
        
        if letter in self.data:
            new_q.append(self.data[letter])
        
        for acc in self.q:
            if letter in acc:
                new_q.append(
                    acc[letter]
                )
        self.q = new_q
        
        for acc in self.q:
            if '$' in acc:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


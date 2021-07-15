class StreamChecker:
    
    history = None

    def __init__(self, words: List[str]):
        self.history = \"\"
        self.index = {}
        for w in words:
            idx = self.index.get(w[-1], [])
            idx.append(w)
            self.index[w[-1]] = idx
        
    def query(self, letter: str) -> bool:
        self.history = self.history + letter
        for word in self.index.get(letter, []):
            if self.history.endswith(word):
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

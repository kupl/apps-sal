class StreamChecker:

    def __init__(self, words: List[str]):
        self.size = len(max(words, key=len))
        self.words = set(words)
        self.curr = \"\"

    def query(self, letter: str) -> bool:
        #try each word with the corresponding last number of letters
        #
        self.curr = self.curr + letter
        self.curr = self.curr[-self.size:]
        for w in self.words:
            length = len(w)
            if self.curr[-length:] == w:
                return True
        
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

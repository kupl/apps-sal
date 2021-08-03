class StreamChecker:

    def __init__(self, words: List[str]):
        self.dict = set([w[::-1] for w in words])
        self.prev = \"\"
        

    def query(self, letter: str) -> bool:
        self.prev = letter + self.prev
        for s in self.dict:
            if self.prev.startswith(s): return True
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

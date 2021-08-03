class StreamChecker:

    def __init__(self, words: List[str]):
        self.dict = list(set(words))
        self.queries = \"\"

    def query(self, letter: str) -> bool:
        self.queries += letter
        for w in self.dict:
            l = len(w)
            # print(self.queries[-l:], w)
            if self.queries[-l:] == w:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

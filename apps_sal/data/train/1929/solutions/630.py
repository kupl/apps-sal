class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = set(words)
        self.queries = ''

    def query(self, letter: str) -> bool:
        self.queries += letter
        for word in self.stream:
            if letter == word[~0]:
                if word == self.queries[-len(word):]:
                    return True
        return False
                
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


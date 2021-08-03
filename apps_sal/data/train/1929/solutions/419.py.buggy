class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = {word[-1]: [] for word in words}
        self.string = \"\"
        for word in words:
            self.words[word[-1]].append(word)
        

    def query(self, letter: str) -> bool:
        self.string += letter
        for word in self.words.get(letter, []):
            if self.string[-1*len(word):] == word:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

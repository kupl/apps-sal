class StreamChecker:

    def __init__(self, words: List[str]):
        self.dictionary = {}
        for word in words:
            current = self.dictionary
            for letter in word:
                if letter not in current:
                    current[letter] = {}
                current = current[letter]
            current['!'] = {}
        self.memory = []

    def query(self, letter: str) -> bool:
        memory = self.memory + [self.dictionary]
        self.memory = []
        validity = False
        for entry in memory:
            if letter in entry:
                self.memory.append(entry[letter])
                if '!' in entry[letter]:
                    validity = True
        return validity


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

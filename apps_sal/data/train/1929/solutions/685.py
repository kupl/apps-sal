class StreamChecker:
    def __init__(self, words: List[str]):
        self.active = []
        self.root = {}

        for word in words:
            current = self.root
            for c in word:
                if c not in current:
                    current[c] = {}
                current = current[c]
            current['word'] = True

    def query(self, letter: str) -> bool:
        self.active = [node[letter] for node in self.active if letter in node]
        if letter in self.root:
            self.active.append(self.root[letter])
        return any('word' in node for node in self.active)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

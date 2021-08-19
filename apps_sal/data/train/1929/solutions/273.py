class StreamChecker:
    def __init__(self, words: List[str]):
        self.s = ''
        self.maxLen = max(len(word) for word in words)

        self.dic = defaultdict(set)

        for word in words:
            self.dic[word[-1]].add(word)

    def query(self, letter: str) -> bool:
        self.s += letter
        self.s = self.s[-self.maxLen:]
        return any(self.s.endswith(w) for w in self.dic[letter])


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

class StreamChecker:

    def __init__(self, words: List[str]):
        self.str = ''
        self.dict_set = collections.defaultdict(set)
        for word in words:
            self.dict_set[word[-1]].add(word)

    def query(self, letter: str) -> bool:
        self.str += letter
        return any(self.str.endswith(word) for word in self.dict_set[letter])


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

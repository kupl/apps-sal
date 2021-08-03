class StreamChecker:
    def __init__(self, words: List[str]):
        self.wordict = {}
        self.word = ''
        for word in words:
            node = self.wordict
            for c in word[::-1]:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node[0] = 0

    def query(self, letter: str) -> bool:
        self.word = self.word + letter
        n = len(self.word)
        nodes = self.wordict
        while n:
            if self.word[n - 1] in nodes:
                if 0 in nodes[self.word[n - 1]]:
                    return True
                else:
                    nodes = nodes[self.word[n - 1]]
                    n -= 1
            else:
                return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

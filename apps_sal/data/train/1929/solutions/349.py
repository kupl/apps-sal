class StreamChecker:

    def __init__(self, words: List[str]):
        self.prefix = {}
        self.maxlen = 0
        for word in words:
            for i in range(len(word) - 1, -1, -1):
                if word[i:][::-1] not in self.prefix:
                    self.prefix[word[i:][::-1]] = 0
            self.prefix[word[::-1]] = 1
            self.maxlen = max(self.maxlen, len(word))
        self.stack = []

    def query(self, letter: str) -> bool:
        self.stack.append(letter)
        for i in range(len(self.stack) - 1, -1, -1):
            if len(self.stack[i:]) > self.maxlen:
                break
            temp = ''.join(self.stack[i:][::-1])
            if temp not in self.prefix:
                return False
            if self.prefix[temp] == 1:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

class StreamChecker:

    def __init__(self, words: List[str]):

        self.wordSet = set(words)
        lSet = set()
        self.lastL = set()
        for word in words:
            lSet.add(len(word))
            self.lastL.add(word[-1])
        self.l = list(lSet)
        self.l.sort()
        self.q = ''

    def query(self, letter: str) -> bool:
        self.q = self.q + letter

        if letter in self.lastL:
            for i in range(len(self.l)):
                if self.l[i] > len(self.q):
                    break
                elif self.q[-self.l[i]:] in self.wordSet:
                    return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

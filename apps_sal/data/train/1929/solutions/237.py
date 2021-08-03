class StreamChecker:

    def __init__(self, words: List[str]):
        self.maxn = max([len(x) for x in words])
        self.suffix = set()
        self.words = set(words)
        for i in words:
            for j in range(len(i) - 1, -1, -1):
                self.suffix.add(i[j:])
        self.queue = []

    def query(self, letter: str) -> bool:
        if len(self.queue) >= self.maxn:
            self.queue.pop(0)
        self.queue.append(letter)
        st = ''
        for i in range(len(self.queue) - 1, -1, -1):
            st = self.queue[i] + st
            if st in self.words:
                return True
            elif st not in self.suffix:
                return False
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

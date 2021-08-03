class StreamChecker:

    def __init__(self, words: List[str]):
        self.memo = {}
        self.words = set()
        words_ = [word[::-1] for word in words]
        for word in words_:
            for i in range(len(word) - 1):
                self.memo[word[:i + 1]] = 0

        for word in words_:
            self.memo[word] = 1

        self.hist = []

        # print(self.memo)

    def query(self, letter: str) -> bool:
        self.hist.insert(0, letter)
        w = ''
        for i in range(len(self.hist)):
            w += self.hist[i]
            # print(w)
            c = self.memo.get(w, None)
            if c is None:
                return False
            if c:
                return True

        return False

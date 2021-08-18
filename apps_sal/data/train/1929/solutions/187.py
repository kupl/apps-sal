class StreamChecker:

    def __init__(self, words: List[str]):
        self.memo = [{} for i in range(2000)]
        self.words = set()
        words_ = [word[::-1] for word in set(words)]
        for word in words_:
            for i in range(len(word) - 1):
                self.memo[i + 1][word[:i + 1]] = 0

        for word in words_:
            self.memo[len(word)][word] = 1

        self.hist = []

    def query(self, letter: str) -> bool:
        self.hist.append(letter)
        w = ''
        for i in range(len(self.hist) - 1, -1, -1):
            w += self.hist[i]
            c = self.memo[len(w)].get(w, None)
            if c is None:
                return False
            if c:
                return True

        return False

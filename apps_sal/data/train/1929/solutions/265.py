class StreamChecker:

    def __init__(self, words: List[str]):
        self.memo = set()
        self.words = set()
        for word in words:
            word_ = word[::-1]
            for i in range(len(word) - 1):
                self.memo.add(word_[:i + 1])
            self.words.add(word_)
        self.hist = []

        print((self.memo))

    def query(self, letter: str) -> bool:
        self.hist.append(letter)
        w = ''
        for i in range(len(self.hist) - 1, -1, -1):
            w += self.hist[i]
            if w in self.words:
                return True
            if w not in self.memo:
                return False

        return False

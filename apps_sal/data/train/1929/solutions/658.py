class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = set(words)
        self.maxx = len(max(self.words, key=len))
        self.tails = set()
        for word in self.words:
            self.tails.add(word[-1])
        self.qs = ''

    def query(self, letter: str) -> bool:
        self.qs += letter
        if len(self.qs) > self.maxx:
            self.qs = self.qs[1:]
        if letter not in self.tails:
            return False
        N = len(self.qs)
        return any((self.qs[i:N] in self.words for i in range(N)))

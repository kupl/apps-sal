class StreamChecker:

    def __init__(self, words: List[str]):
        self.tries = {}
        for word in words:
            tries = self.tries
            for c in word:
                if c not in tries:
                    tries[c] = {}
                tries = tries[c]
            tries['END'] = 1
        self.pool = []

    def query(self, letter: str) -> bool:
        new_pool = []
        self.pool.append(self.tries)
        for tries in self.pool:
            if letter in tries:
                new_pool.append(tries[letter])
        self.pool = new_pool
        return any('END' in tries for tries in self.pool)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

class StreamChecker:

    def __init__(self, words: List[str]):
        self.d = defaultdict(dict)
        for word in words:
            word = word[::-1]
            d = self.d
            for c in word[:-1]:
                d[c] = d.get(c) or defaultdict(dict)
                d = d[c]
            c = word[-1]
            if c not in d:
                d[c] = {'0': 1}
            else:
                d[c]['0'] = 1
            self.queue = []

    def query(self, letter: str) -> bool:
        self.queue.append(letter)
        d = self.d
        for c in self.queue[::-1]:
            if c in d:
                d = d[c]
                if '0' in d:
                    return True
            else:
                break
        return False

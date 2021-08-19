class StreamChecker:

    def __init__(self, words: List[str]):
        self.map = {}
        self.history = ''
        for w in words:
            curr = self.map
            w = w[::-1]
            w += '0'
            for c in w:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]

    def query(self, letter: str) -> bool:
        self.history += letter
        curr = self.map
        for c in self.history[::-1]:
            if c not in curr:
                break
            curr = curr[c]
            if '0' in curr:
                return True
        return False

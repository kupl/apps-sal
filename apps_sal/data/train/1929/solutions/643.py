class StreamChecker:

    def __init__(self, words: List[str]):
        self.t = {}
        for word in words:
            curr = self.t
            for i in word[::-1]:
                if i not in curr:
                    curr[i] = {}
                curr = curr[i]
            curr['end'] = True
        self.s = ''

    def query(self, letter: str) -> bool:
        self.s += letter
        curr = self.t
        for i in self.s[::-1]:
            if i not in curr:
                return False
            if i in curr:
                curr = curr[i]
            if 'end' in curr:
                return True
        return False

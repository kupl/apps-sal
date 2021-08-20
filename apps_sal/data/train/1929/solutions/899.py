class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = {}
        self.state = []
        for word in words:
            curr = self.root
            for c in list(word):
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['*'] = {}

    def query(self, letter: str) -> bool:
        ret = False
        new_state = []
        if letter in self.root:
            self.state.append(self.root)
        for s in self.state:
            if letter in s:
                s = s[letter]
                if '*' in s:
                    ret = True
                new_state.append(s)
        self.state = new_state
        return ret

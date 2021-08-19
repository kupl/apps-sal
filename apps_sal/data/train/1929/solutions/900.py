class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.letters = []
        for w in words:
            cur = self.trie
            for l in w[::-1]:
                if not l in cur:
                    cur[l] = {}
                cur = cur[l]
            cur['end'] = {}

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        cur = self.trie
        for l in self.letters[::-1]:
            if not l in cur:
                return False
            cur = cur[l]
            if 'end' in cur:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

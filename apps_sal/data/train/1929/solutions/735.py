class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for w in words:
            curr = self.trie
            for c in w+\"#\":
                curr = curr.setdefault(c, {})
        self.matching = []

    def query(self, letter: str) -> bool:
        if letter in self.trie:
            self.matching.append(self.trie)
        res = []
        ans = False
        for i in self.matching:
            if letter in i:
                res.append(i[letter])
                if \"#\" in i[letter]:
                    ans = True
        self.matching = res
        return ans
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            cur = self.trie
            for ch in word:
                if ch not in cur:
                    cur[ch] = {}
                cur = cur[ch]
            cur['#'] = '#'
        self.queue = []

    def query(self, letter: str) -> bool:
        res = False
        nxt = []
        for top in self.queue:
            if letter in top:
                if '#' in top[letter]:
                    res = True
                nxt.append(top[letter])
        if letter in self.trie:
            if '#' in self.trie[letter]:
                res = True
            nxt.append(self.trie[letter])
        self.queue = nxt
        return res


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

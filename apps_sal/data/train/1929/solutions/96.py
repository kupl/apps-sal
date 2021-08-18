class StreamChecker:

    def __init__(self, words: List[str]):
        self.flag = []
        self.trie = {}
        for word in words:
            cur = self.trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['.'] = {}

    def query(self, letter: str) -> bool:
        if letter in self.trie:
            self.flag.append(self.trie)
        res = False
        new_flag = []
        for f in self.flag:
            if letter in f:
                new_flag.append(f[letter])
                if '.' in f[letter]:
                    res = True
        self.flag = new_flag
        return res

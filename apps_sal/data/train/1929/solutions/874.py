class StreamChecker:

    def __init__(self, words: List[str]):

        self.trie = {}

        for word in words:
            cur = self.trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['end'] = None

        self.buffer = []

    def query(self, letter: str) -> bool:

        found = False
        swap = []
        if letter in self.trie:
            swap.append(self.trie[letter])
            found = 'end' in self.trie[letter]

        for b in self.buffer:
            if letter in b:
                swap.append(b[letter])
                if 'end' in b[letter]:
                    found = True
        self.buffer = swap
        return found


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

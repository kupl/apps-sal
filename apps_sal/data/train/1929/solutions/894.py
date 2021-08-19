# 08-23-2020
# Day 23 stream of characters

class StreamChecker:

    def __init__(self, words: List[str]):

        trie = dict()
        for word in words:
            t = trie
            for c in word:
                if not c in t:
                    t[c] = dict()
                t = t[c]

            t[None] = True

        self.trie = trie
        self.current_tries = []

    def query(self, letter: str) -> bool:
        new_tries = []
        res = False
        for trie in self.current_tries:
            if letter in trie:
                trie = trie[letter]
                new_tries.append(trie)

                res = res | trie.get(None, False)

        if letter in self.trie:
            t = self.trie.copy()
            t = t[letter]
            res = res | t.get(None, False)
            new_tries.append(t)

        self.current_tries = new_tries

        return res


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

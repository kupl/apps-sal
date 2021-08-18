class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.pointers = [self.trie]
        for word in words:
            t = self.trie
            for w in word:
                if w not in t:
                    t[w] = {}
                t = t[w]
            t['
        print((self.trie))

    def query(self, letter: str) -> bool:
        s = [self.trie]
        for ele in self.pointers:
            if letter in ele:
                s.append(ele[letter])
        self.pointers = s
        return any(['

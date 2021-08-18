class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node['end'] = True
        self.s = []

    def query(self, letter: str) -> bool:
        f = 0
        temp = []
        self.s.append(self.trie)
        for d in self.s:
            if letter in d:
                t = d[letter]
                f |= 'end' in t
                temp.append(t)
        self.s = temp
        return f

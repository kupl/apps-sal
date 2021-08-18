class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = dict()
        for word in words:
            node = self.trie
            for c in word[::-1]:
                if c not in node:
                    node[c] = dict()
                node = node[c]
            node['.'] = '.'

        self.syms = []

    def query(self, letter: str) -> bool:
        trie, syms = self.trie, self.syms

        syms.append(letter)

        node = trie
        for c in syms[::-1]:
            if c not in node:
                return False
            node = node[c]
            if '.' in node:
                return True

        return False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            node = self.trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['#'] = {}
        self.table = []

    def query(self, letter: str) -> bool:
        tmp = []
        for node in self.table + [self.trie]:
            if letter in node:
                tmp.append(node[letter])
        self.table = tmp
        return any(('#' in node for node in self.table))

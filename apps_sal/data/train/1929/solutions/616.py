class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = defaultdict(dict)
        for word in words:
            node = self.trie
            for i in word[::-1]:
                if i not in node:
                    node[i] = {}
                node = node[i]
            node['
        self.q = ''

    def query(self, letter: str) -> bool:
        self.q += letter
        node = self.trie
        for i in self.q[::-1]:
            if '
                return True
            if i not in node:
                return False
            node = node[i]
        return '

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = deque([])

        for w in words:
            node = self.trie
            for c in w[::-1]:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['$'] = w

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)

        node = self.trie
        for c in self.stream:
            if '$' in node:
                return True
            if c not in node:
                return False
            node = node[c]
        return '$' in node

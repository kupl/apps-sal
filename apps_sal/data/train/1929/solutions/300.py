class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = collections.deque()
        for word in words:
            node = self.trie
            for ch in word[::-1]:
                if not ch in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = word

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        node = self.trie
        for c in self.stream:
            if '$' in node:
                return True
            if not c in node:
                return False
            node = node[c]
        return '$' in node

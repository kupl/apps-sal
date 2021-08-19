class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            node = self.trie
            for c in word[::-1]:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['$'] = True
        self.queries = ''
        self.W = max(list(map(len, words)))

    def query(self, letter: str) -> bool:
        ret = False
        self.queries += letter
        node = self.trie
        for c in self.queries[::-1][:self.W]:
            if c in node:
                node = node[c]
                if '$' in node:
                    return True
            else:
                return False
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

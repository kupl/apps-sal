class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            node = self.trie
            for c in word:
                try:
                    node = node[c]
                except KeyError:
                    n = node[c] = {}
                    node = n
            node['$'] = None
        self.index = 0
        self.nodes = {}

    def query(self, letter: str) -> bool:
        nodes = {}
        self.nodes[self.index] = self.trie
        for i, node in list(self.nodes.items()):
            try:
                nodes[i] = node[letter]
            except KeyError:
                pass
        
        self.nodes = nodes
        self.index += 1
        return any('$' in node for node in list(nodes.values()))
                


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            root = self.trie
            for ch in word:
                if not ch in root:
                    root[ch] = {}
                root = root[ch]
            root['#'] = '#'

        self.nodes = [self.trie]

    def query(self, letter: str) -> bool:
        new_nodes = [self.trie]
        res = False
        for node in self.nodes:
            if letter in node:
                new_node = node[letter]
                if '#' in new_node:
                    res = True
                new_nodes.append(new_node)
        self.nodes = new_nodes
        return res


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

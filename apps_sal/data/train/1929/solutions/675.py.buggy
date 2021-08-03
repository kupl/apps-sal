IS_CHAR = \".\"

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            node = self.trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node[IS_CHAR] = word

        self.active_nodes = []

    def query(self, letter: str) -> bool:
        self.active_nodes = [node[letter] for node in self.active_nodes + [self.trie,] if letter in node]
        return any(IS_CHAR in node for node in self.active_nodes)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

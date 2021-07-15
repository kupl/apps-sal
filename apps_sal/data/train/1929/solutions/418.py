class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.s = \"\"
        for w in words:
            node = self.trie
            for c in w[::-1]:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['#'] = True

    def query(self, letter: str) -> bool:
        self.s = letter+self.s
        node = self.trie
        for c in self.s:
            if c in node:
                node = node[c]
            else:
                return False
            if '#' in node:
                return True
        
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            node = self.trie
            for c in word[::-1]:
                node = node.setdefault(c, {})
            node[\"$\"] = True
        self.stream = collections.deque([])
        
    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        node = self.trie
        for c in self.stream:
            if '$' in node:
                return True
            if c not in node:
                return False
            node = node[c]
        return \"$\" in node


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

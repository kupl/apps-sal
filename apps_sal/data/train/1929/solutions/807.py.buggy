class StreamChecker:

    def __init__(self, words: List[str]):
        self.tree = {}
        for word in words:
            node = self.tree
            for c in word:
                node = node.setdefault(c, {})
            node['#'] = True
        self.active_match = []

    def query(self, letter: str) -> bool:
        assert len(letter) == 1, \"letter should have length 1\"
        to_delete = []
        for i, m in enumerate(self.active_match):
            if letter in m:
                self.active_match[i] = m[letter]
            else:
                to_delete.append(i)
        for i in reversed(to_delete):
            self.active_match[i] = self.active_match[-1]
            self.active_match.pop()
        if letter in self.tree:
            self.active_match.append(self.tree[letter])
        for m in self.active_match:
            if '#' in m:
                return True
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

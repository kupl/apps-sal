class StreamChecker:
    def __init__(self, words: List[str]):
        self.string = collections.deque()
        self.root = {}
        for word in words:
            node = self.root
            for c in word[::-1]:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['#'] = 1

    def query(self, letter: str) -> bool:
        self.string.appendleft(letter)
        node = self.root
        for c in self.string:
            if c in node:
                node = node[c]
                if '#' in node:
                    return True
            else:
                return False
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.history = collections.deque()
        self.N = 0
        for word in words:
            self.N = max(self.N, len(word))
            rword = word[::-1]
            node = self.trie
            for ch in rword:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node[\"#\"] = {}

    def query(self, letter: str) -> bool:
        self.history.appendleft(letter)
        if len(self.history) > self.N:
            self.history.pop()
        node = self.trie
        for ch in self.history:
            if ch not in node:
                return False
            node = node[ch]
            if \"#\" in node:
                return True
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

class StreamChecker:

    def __init__(self, words: List[str]):
        trie = lambda: defaultdict(trie)
        self.trie = trie()
        for word in words:
            current = self.trie
            for ch in word[::-1]:
                current = current[ch]
            current.setdefault(\"#end#\")
        self.stack = []

    def query(self, letter: str) -> bool:
        self.stack.append(letter)
        state_trie = self.trie
        for pos in range(len(self.stack) - 1, -1, -1):
            ch = self.stack[pos]
            if ch in state_trie and \"#end#\" in state_trie[ch]:
                return True
            elif ch not in state_trie:
                return False
            state_trie = state_trie[ch]
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

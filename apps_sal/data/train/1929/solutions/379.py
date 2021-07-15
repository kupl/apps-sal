class StreamChecker:
    END = \"#\"

    def __init__(self, words: List[str]):
        self.trie = self.build_trie(words)
        self.prefix = collections.deque()
        
    def build_trie(self, words: list):
        trie = {}
        for word in words:
            root = trie
            for char in reversed(word):
                root = root.setdefault(char, {})
            root[self.END] = word
        return trie

    def query(self, letter: str) -> bool:
        self.prefix.appendleft(letter)
        root = self.trie
        
        for char in self.prefix:
            if char in root:
                root = root[char]
                if self.END in root:
                    return True
            else:
                break
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

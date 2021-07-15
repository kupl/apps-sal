class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = collections.defaultdict()
        for word in words:
            root = self.trie
            for c in word:
                root = root.setdefault(c, {})
            root[\"#\"] = \"#\"
        self.cache = []
    
    def query(self, letter: str) -> bool:
        next_cache = []
        for node in self.cache + [self.trie]:
            if letter in node:
                next_cache.append(node[letter])
        self.cache = next_cache
        for node in self.cache:
            if '#' in node:
                return True
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

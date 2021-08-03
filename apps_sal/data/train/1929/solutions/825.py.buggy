class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        # #-means end of word and @-means query pointer
        for word in words:
            cur = self.trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur[\"#\"] = True
        self.pointers = [self.trie]
        self.ends = set()
        self.waiting = []

    def query(self, letter: str) -> bool:
        
        self.waiting = [node[letter] for node in self.waiting + [self.trie] if letter in node]
        return any(\"#\" in node for node in self.waiting)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


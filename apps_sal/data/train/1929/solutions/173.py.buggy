class StreamChecker:

    def __init__(self, words: List[str]):
        Trie = lambda: collections.defaultdict(Trie)
        self.trie = Trie()
        for word in words:
            reduce(dict.__getitem__, word[::-1] + \"$\", self.trie)
        self.queries = \"\"

    def query(self, letter: str) -> bool:
        self.queries += letter
        curr = self.trie
        #print(\"query\")
        for i in range(len(self.queries)-1, -1, -1):
            c = self.queries[i]
            if \"$\" in curr:
                return True
            if c not in curr:
                return False
            curr = curr[c]
        return \"$\" in curr


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

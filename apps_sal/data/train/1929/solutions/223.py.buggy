class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            word = word[::-1]
            cur = self.trie
            for char in word:
                if char not in cur:
                    cur[char] = {}
                cur = cur[char]
            cur['$'] = {}
        self.queries = []

    def query(self, letter: str) -> bool:
        self.queries.insert(0, letter)
        cur = self.trie
        for char in self.queries:
            if '$' in cur:
                return True
            if char not in cur:
                return False
            cur = cur[char]
        return ('$' in cur)

    def __repr__(self):
        return \"Trie: \" + str(self.trie) + \"\
\" + \"Queries: \" + str(self.queries)





# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

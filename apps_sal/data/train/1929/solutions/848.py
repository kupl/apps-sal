class StreamChecker:

    def __init__(self, words: List[str]):
        trie = {}
        for word in words:
            ptr = trie
            for c in word:
                if c not in ptr:
                    ptr[c] = {}
                ptr = ptr[c]
            ptr[\"term\"] = True
        self.trie = trie
        self.curr = []
                
    def query(self, letter: str) -> bool:
        # add new start
        self.curr.append(self.trie)
        # progress
        new_curr = []
        res = False
        for ptr in self.curr:
            if letter in ptr:
                ptr = ptr[letter]
                if not res and ptr.get(\"term\", False):
                    res = True
                new_curr.append(ptr)
        self.curr = new_curr
        return res


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

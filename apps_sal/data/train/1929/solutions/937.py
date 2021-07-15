class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        
        for word in words:
            node = self.trie
            for c in word:
                node = node.setdefault(c, {})
            node[\"*\"] = None
        self.cur = [self.trie]

    def query(self, letter: str) -> bool:
        ans = False
        new = [self.trie]
        for node in self.cur:
            if letter in node:
                new.append(node[letter])
                if not ans and \"*\" in node[letter]:
                    ans = True
        
        self.cur = new
        return ans
                


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

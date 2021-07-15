class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = trie = {}
        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node['*'] = word
        self.candidates = []

    def query(self, letter: str) -> bool:
        new = []
        exists = False
        for candidate in self.candidates + [self.trie]:
            if letter in candidate:
                new.append(candidate[letter])
                if candidate[letter].get('*'):
                    exists = True
        self.candidates = new
        return exists
                


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


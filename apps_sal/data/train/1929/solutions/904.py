class StreamChecker:
    prefixes = []

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            d = self.trie
            for letter in word:
                if letter not in d:
                    d[letter] = {}
                d = d[letter]
            d['end'] = True

    def query(self, letter: str) -> bool:
        self.prefixes = [node[letter] for node in self.prefixes + [self.trie] if letter in node]
        # if letter in self.trie:
        #     self.prefixes.append(self.trie[letter])
        return any('end' in node for node in self.prefixes)
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


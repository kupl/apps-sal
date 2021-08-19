class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            self.trie_insert(word)
        self.searches = []

    def trie_insert(self, word):
        curr = self.trie
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr['*'] = True  # mark last node as a word

    def query(self, letter: str) -> bool:
        self.searches.append(self.trie)
        self.searches = [node.get(letter) for node in self.searches if letter in node]
        return any('*' in node for node in self.searches)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

class StreamChecker:

    def __init__(self, words):
        T = lambda: collections.defaultdict(T)
        self.trie = T()
        for w in words: reduce(dict.__getitem__, w, self.trie)['#'] = True
        self.waiting = []

    def query(self, letter):
        self.waiting = [node[letter] for node in self.waiting + [self.trie] if letter in node]
        return any(\"#\" in node for node in self.waiting)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

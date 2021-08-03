class StreamChecker(object):

    def __init__(self, word):
        T = lambda: collections.defaultdict(T)
        self.trie = T()
        for w in word: reduce(dict.__getitem__, w, self.trie)['#'] = True
        self.waiting = []

    def query(self, letter):
        self.waiting = [node[letter] for node in self.waiting + [self.trie] if letter in node]
        return any(\"#\" in node for node in self.waiting)

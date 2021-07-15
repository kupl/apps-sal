class StreamChecker(object):

    def __init__(self, words):
        self.word_map, self.len_map, self.buffer = defaultdict(set), defaultdict(set), \"\"
        for w in words:
            self.word_map[w[-1]].add(w[::-1])
            self.len_map[w[-1]].add(len(w))
        

    def query(self, letter):
        self.buffer = letter + self.buffer
        return any(len(self.buffer) >= l and self.buffer[:l] in self.word_map[letter] for l in self.len_map[letter])


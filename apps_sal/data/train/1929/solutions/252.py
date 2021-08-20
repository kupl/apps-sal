class Trie:
    d = {}
    record = {}

    def __init__(self):
        self.record = {}
        self.d = {}

    def add(self, word):
        if len(word) == 1:
            if word[0] not in self.d:
                self.d[word[0]] = Trie()
                self.d[word[0]].d[-1] = 1
                return
            else:
                self.d[word[0]].d[-1] = 1
                return
        letter = word[-1]
        if letter in self.d:
            self.d[letter].add(word[:-1])
            return
        self.d[letter] = Trie()
        self.d[letter].add(word[:-1])
        return

    def search(self, ls, index):
        if index in self.record:
            return self.record[index]
        val = False
        if -1 in self.d:
            val = True
        elif index < 0:
            val = False
        elif ls[index] in self.d:
            val = self.d[ls[index]].search(ls, index - 1)
        self.record[index] = val
        return val


class StreamChecker:
    root = None
    l = None
    size = 0

    def __init__(self, words: List[str]):
        self.root = Trie()
        self.l = collections.deque()
        self.size = 0
        for i in words:
            self.root.add(i)

    def query(self, letter: str) -> bool:
        self.size += 1
        self.l.append(letter)
        return self.root.search(self.l, self.size - 1)

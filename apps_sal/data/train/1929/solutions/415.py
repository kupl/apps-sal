class Trie:
    def __init__(self, end=False):
        self.child = dict()
        self.end = end

    def add(self, word, i=0):
        if i >= len(word):
            return
        if word[i] not in self.child:
            self.child[word[i]] = Trie()
        if i == len(word) - 1:
            self.child[word[i]].end = True
        self.child[word[i]].add(word, i + 1)

class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Trie()
        for word in words:
            self.root.add(word[::-1])
        self.stream = ''

    def query(self, letter: str) -> bool:
        self.stream = letter + self.stream
        ptr = self.root
        for c in self.stream:
            if c in ptr.child:
                ptr = ptr.child[c]
                if ptr.end:
                    return True
            else:
                break
        return False

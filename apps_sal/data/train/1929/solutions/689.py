class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.words = [word[::-1] for word in words]
        self.string = ''
        self.l = 0
        self.createTrie()

    def createTrie(self):
        for i in self.words:
            t = self.trie
            for j in i:
                if j not in t:
                    t[j] = dict()
                t = t[j]
            t['*'] = dict()

    def searchTrie(self, word):
        trie = self.trie
        for i in word:
            if i in trie:
                trie = trie[i]
            else:
                return False
        return '*' in trie

    def query(self, letter: str) -> bool:
        self.string += letter
        self.l += 1
        trie = self.trie
        for i in self.string[::-1]:
            if i in trie:
                trie = trie[i]
                if '*' in trie:
                    return True
            else:
                return False
        return False

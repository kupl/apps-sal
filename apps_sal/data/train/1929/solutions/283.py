class Trie:
    def __init__(self):
        self.Trie = {}

    def insert(self, word):
        curr = self.Trie

        for i in word:
            if i not in curr:
                curr[i] = {}
            curr = curr[i]
        curr['

    def search(self, word):
        curr = self.Trie

        for i in word:
            if i not in curr:
                return False
            else:
                if '
                    return True
            curr = curr[i]
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.dictTree = Trie()
        self.queryStream = list()

        for i in words:
            self.dictTree.insert(i[::-1])

    def query(self, letter: str) -> bool:
        self.queryStream[0:0] = letter
        return self.dictTree.search(self.queryStream)

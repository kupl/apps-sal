class TrieNode:

    def __init__(self):
        self.children = collections.defaultdict(lambda: TrieNode())
        self.word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.word = True

    def search(self, word, prefix=False):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        if prefix:
            return True
        return node.word

    def starswith(self, prefix):
        return self.search(prefix, True)


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for w in words:
            self.trie.insert(w[::-1])
        self.stream = []

    def query(self, letter: str) -> bool:
        self.stream += [letter]
        for i in range(1, len(self.stream) + 1):
            if not self.trie.search(self.stream[-i:][::-1], True):
                return False
            if self.trie.search(self.stream[-i:][::-1]):
                return True

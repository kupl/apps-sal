class WordNode:
    def __init__(self):
        self.children = [None] * 26
        self.isFront = False


class WordTrie:
    def __init__(self):
        self.head = WordNode()

    def addWord(self, word):
        node = self.head
        for c in word[::-1]:
            if not node.children[ord(c) - ord('a')]:
                node.children[ord(c) - ord('a')] = WordNode()
            node = node.children[ord(c) - ord('a')]
        node.isFront = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.Trie = WordTrie()
        for w in words:
            self.Trie.addWord(w)
        self.queries = []

    def query(self, letter: str) -> bool:
        self.queries.append(letter)
        node = self.Trie.head
        for l in self.queries[::-1]:
            if not node.children[ord(l) - ord('a')]:
                return False
            node = node.children[ord(l) - ord('a')]
            if node.isFront:
                return True
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

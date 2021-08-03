class trie:
    def __init__(self, val=None):
        self.val = val
        self.next = {}
        self.is_complete = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = trie()
        # insert all words in trie
        for w in words:
            node = self.root
            for c in w[::-1]:
                if c not in node.__next__:
                    node.next[c] = trie(c)
                node = node.next[c]
            node.is_complete = True

        # to keep track of previous queries
        self.queries = []

    def query(self, letter: str) -> bool:
        self.queries.append(letter)

        ### search in trie
        node = self.root
        for c in self.queries[::-1]:
            if c not in node.__next__:
                return False
            node = node.next[c]
            if node.is_complete:
                return True

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

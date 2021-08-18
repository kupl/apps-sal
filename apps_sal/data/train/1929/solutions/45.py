class trie:
    def __init__(self, val=None):
        self.val = val
        self.next = {}
        self.is_complete = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = trie()
        for w in words:
            node = self.root
            for c in w[::-1]:
                if c not in node.__next__:
                    node.next[c] = trie(c)
                node = node.next[c]
            node.is_complete = True

        self.queries = []

    def query(self, letter: str) -> bool:
        self.queries.append(letter)

        node = self.root
        for c in self.queries[::-1]:
            if c not in node.__next__:
                return False
            node = node.next[c]
            if node.is_complete:
                return True

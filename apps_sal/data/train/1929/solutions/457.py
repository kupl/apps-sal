class trie:

    def __init__(self, val=None):
        self.val = val
        self.next = {}
        self.is_complete = False


'\n### https://youtu.be/Y37WA4advWw\n\nLogic here is to make trie of given works in reverse order ..so that if we want to find whether upto this point any query make sense...we can check in reverse order\n\n'


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
        self.queries.insert(0, letter)
        node = self.root
        for c in self.queries:
            if c not in node.__next__:
                return False
            node = node.next[c]
            if node.is_complete:
                return True

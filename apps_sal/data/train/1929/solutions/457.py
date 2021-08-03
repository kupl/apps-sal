class trie:
    def __init__(self, val=None):
        self.val = val
        self.next = {}
        self.is_complete = False


'''
### https://youtu.be/Y37WA4advWw

Logic here is to make trie of given works in reverse order ..so that if we want to find whether upto this point any query make sense...we can check in reverse order

'''


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
        self.queries.insert(0, letter)

        ### search in trie
        node = self.root
        for c in self.queries:
            if c not in node.__next__:
                return False
            node = node.next[c]
            if node.is_complete:
                return True

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

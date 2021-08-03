class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
        root.end_node = 1


class StreamChecker:
    def __init__(self, words):
        self.trie = Trie()
        self.Stream = deque()
        for word in words:
            self.trie.insert(word[::-1])

    def query(self, letter):
        self.Stream.appendleft(letter)
        cur = self.trie.root

        for c in self.Stream:
            if c in cur.children:
                cur = cur.children[c]
                if cur.end_node:
                    return True
            else:
                break
        return False

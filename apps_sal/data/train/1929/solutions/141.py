class TrieNode:

    def __init__(self):
        self.children = {}
        self.ends_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())
        node.ends_word = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.deque = deque()
        for w in words:
            self.trie.insert(reversed(w))

    def query(self, letter: str) -> bool:
        self.deque.appendleft(letter)
        if len(self.deque) > 2000:
            self.deque.pop()
        node = self.trie.root
        for c in self.deque:
            node = node.children.get(c)
            if not node:
                return False
            if node.ends_word:
                return True
        return False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
        self.cache = ''

    def query(self, letter: str) -> bool:
        self.cache = letter + self.cache
        return self.trie.find(self.cache)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            cur.children.setdefault(c, TrieNode())
            cur = cur.children[c]
        cur.is_word = True

    def find(self, word):
        cur = self.root
        for c in word:
            if cur.is_word:
                return True
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.is_word


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

class TrieNode:

    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def build(self, words):
        for word in words:
            self._insert(word[::-1])

    def _insert(self, word):
        cur = self.root
        for char in word:
            cur = cur.children[char]
        cur.is_word = True

    def search(self, stream):
        cur = self.root
        for char in stream[::-1]:
            if char in cur.children:
                cur = cur.children[char]
                if cur.is_word:
                    return True
            else:
                return False
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.trie.build(words)
        self.stream = ''

    def query(self, letter: str) -> bool:
        self.stream += letter
        found = self.trie.search(self.stream)
        return found


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

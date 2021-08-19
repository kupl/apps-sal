class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            if node.children[c].is_word:
                return True
            node = node.children[c]
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.input = deque()
        self.trie = Trie()
        self.max_len = 0
        for word in words:
            self.trie.add_word(word[::-1])
            self.max_len = max(self.max_len, len(word))

    def query(self, letter: str) -> bool:
        self.input.appendleft(letter)
        if len(self.input) > self.max_len:
            self.input.pop()
        return self.trie.search_word(self.input)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

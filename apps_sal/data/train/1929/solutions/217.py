class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.stream = collections.deque()
        self.size = 0

        for word in words:
            self.size = max(len(word), self.size)
            self.trie.add_word(word[::-1])

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)

        if len(self.stream) > self.size:
            self.stream.pop()

        node = self.trie.root
        for ch in self.stream:
            if node.is_word:
                return True
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word

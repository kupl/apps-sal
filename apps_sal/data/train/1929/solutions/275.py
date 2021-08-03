class TrieNode:
    def __init__(self):
        self.children, self.end_node = {}, 0


class Trie:
    def __init__(self, ):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root

        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())

        root.end_node = 1


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.stream = deque()
        for word in words:
            self.trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        current = self.trie.root

        for char in self.stream:
            if char in current.children:
                current = current.children[char]
                if current.end_node:
                    return True
            else:
                break

        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for char in word:
            root = root.children.setdefault(char, TrieNode())
        root.end = 1


class StreamChecker:

    def __init__(self, words: List[str]):
        self.Trie = Trie()
        self.QueryBuffer = deque()
        for word in words:
            self.Trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        self.QueryBuffer.appendleft(letter)
        cur = self.Trie.root
        for char in self.QueryBuffer:
            if char in cur.children:
                cur = cur.children[char]
                if cur.end == 1:
                    return True
            else:
                break
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

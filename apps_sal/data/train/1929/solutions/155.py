class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_complete = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for char in word[:: -1]:
            cur = cur.children.setdefault(char, TrieNode())
        cur.is_complete = True


class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.stream = deque()
        for word in words:
            self.trie.insert(word)

    def query(self, letter: str) -> bool:
        cur = self.trie.root
        self.stream.appendleft(letter)
        for s in self.stream:
            if s in list(cur.children.keys()):
                cur = cur.children[s]
                if cur.is_complete:
                    return True
            else:
                break
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

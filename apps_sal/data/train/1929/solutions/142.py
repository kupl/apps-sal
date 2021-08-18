class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for c in word:
            root = root.children.setdefault(c, TrieNode())
        root.isWord = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
        self.stream = deque()

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        curr = self.trie.root

        for c in self.stream:
            if c in curr.children:
                curr = curr.children[c]
                if curr.isWord:
                    return True
            else:
                break

        return False

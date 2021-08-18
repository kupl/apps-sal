class TrieNode:

    def __init__(self):
        self.children = {}
        self.end_node = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        root = self.root
        for w in word:
            root = root.children.setdefault(w, TrieNode())
        root.end_node = 1


class StreamChecker:

    def __init__(self, words: List[str]):
        self.t = Trie()
        self.stream = deque()
        for w in words:
            self.t.insert(w[::-1])

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        t = self.t.root
        for curr in self.stream:
            if curr in t.children:
                t = t.children[curr]
                if t.end_node:
                    return True
            else:
                break
        return False

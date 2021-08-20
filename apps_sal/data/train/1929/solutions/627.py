class TrieNode:

    def __init__(self):
        self.children = {}
        self.terminal = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.queue = collections.deque()
        self.words = words
        self.root = TrieNode()
        for word in self.words:
            node = self.root
            for c in reversed(word):
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.terminal = True

    def query(self, letter: str) -> bool:
        self.queue.appendleft(letter)
        node = self.root
        if letter in node.children:
            for l in self.queue:
                if l in node.children:
                    node = node.children[l]
                    if node.terminal:
                        return True
                else:
                    return False

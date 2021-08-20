class TrieNode:

    def __init__(self):
        self.is_word = False
        self.children = {}


class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = deque()
        self.root = TrieNode()
        for word in words:
            node = self.root
            for ch in word[::-1]:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_word = True

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        node = self.root
        for ch in self.stream:
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.is_word:
                return True
        return False

class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.prefix = ''
        for word in words:
            node = self.root
            for c in word[::-1]:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.is_word = True

    def query(self, letter: str) -> bool:
        self.prefix += letter
        node = self.root
        for c in self.prefix[::-1]:
            if c not in node.children:
                return False
            node = node.children[c]
            if node.is_word:
                return True
        return False

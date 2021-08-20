class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.end = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for word in words:
            node = self.root
            for ch in word[::-1]:
                ind = ord(ch) - ord('a')
                if node.children[ind] is None:
                    node.children[ind] = TrieNode()
                node = node.children[ind]
            node.end = True
        self.hist = ''

    def query(self, letter: str) -> bool:
        self.hist = letter + self.hist
        node = self.root
        for ch in self.hist:
            ind = ord(ch) - ord('a')
            if node.children[ind] is None:
                return False
            node = node.children[ind]
            if node.end:
                return True
        return False

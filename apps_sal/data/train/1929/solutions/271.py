class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.buffer = ''
        self.letters = []
        for word in words:
            word = word[::-1]
            node = self.root
            for c in word:
                node = node.children[c]
            node.isEnd = True

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        i = len(self.letters) - 1
        node = self.root
        while i >= 0:
            if node.isEnd:
                return True
            if self.letters[i] not in node.children:
                return False
            node = node.children[self.letters[i]]
            i -= 1
        return node.isEnd


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isEnd = False

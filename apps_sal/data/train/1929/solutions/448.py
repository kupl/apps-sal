class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.s = []
        for word in words:
            current = self.root
            for w in reversed(word):
                current = current.children[w]
            current.is_end = True

    def query(self, letter: str) -> bool:
        self.s.append(letter)
        current = self.root
        for w in reversed(self.s):
            if w not in current.children:
                break
            current = current.children[w]
            if current.is_end:
                return True
        return False

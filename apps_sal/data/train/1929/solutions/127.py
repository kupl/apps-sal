class TrieNode:
    def __init__(self):
        self.end = False
        self.children = [None] * 26


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.cand = []
        self.maxlen = float('-inf')
        for w in words:
            self.insert(w)
            self.maxlen = max(self.maxlen, len(w))

    def insert(self, s):
        node = self.root
        for c in s[::-1]:
            index = ord(c) - ord('a')
            if node.children[index] is None:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.end = True

    def query(self, letter: str) -> bool:
        self.cand.insert(0, letter)

        if len(self.cand) > self.maxlen:
            self.cand.pop()

        curr = self.root

        for c in self.cand:
            if curr.children[ord(c) - ord('a')] is not None:
                curr = curr.children[ord(c) - ord('a')]
                if curr.end:
                    return True
            else:
                return False

        return False

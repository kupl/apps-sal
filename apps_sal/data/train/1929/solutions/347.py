class TrieNode:

    def __init__(self):
        self.fin = ''
        self.children = {}

    def add(self, s, i=0):
        if i == len(s):
            self.fin = s
            return
        if s[i] not in self.children:
            self.children[s[i]] = TrieNode()
        self.children[s[i]].add(s, i + 1)

    def get(self, c):
        result = self.children.get(c, None)
        return result


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for w in words:
            self.root.add(w[::-1])
        self.hist = []

    def query(self, letter: str) -> bool:
        self.hist.append(letter)
        node = self.root
        for l in reversed(self.hist):
            node = node.get(l)
            if node is None:
                return False
            if node.fin:
                return True
        return False

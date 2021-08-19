class StreamChecker:

    class Node:
        def __init__(self):
            self.end = False
            self.child = dict()

    def __init__(self, words: List[str]):
        self._root = self.Node()
        self.seq = []

        def insert(word=''):
            node = self._root
            for c in reversed(word):
                if c not in node.child:
                    node.child[c] = self.Node()
                node = node.child[c]
            node.end = True

        for word in words:
            insert(word)

    def _search(self) -> bool:
        node = self._root
        ind = len(self.seq)
        while ind:
            node = node.child.get(self.seq[ind - 1], None)
            if not node:
                return False
            if node.end:
                return True
            ind -= 1
        return False

    def query(self, letter: str) -> bool:
        self.seq.append(letter)
        if len(self.seq) > 2000:
            self.seq.pop(0)
        return self._search()


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

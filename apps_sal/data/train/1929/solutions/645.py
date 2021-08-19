class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = {}
        self.end = -1
        for w in words:
            self.insert(w)
        self.qhist = ''

    def insert(self, word):
        curNode = self.root
        for c in word[::-1]:
            if not c in curNode:
                curNode[c] = {}
            curNode = curNode[c]
        curNode[self.end] = True

    def query(self, letter: str) -> bool:
        self.qhist += letter
        curNode = self.root
        for c in self.qhist[::-1]:
            if not c in curNode:
                return False
            curNode = curNode[c]
            if self.end in curNode:
                return True

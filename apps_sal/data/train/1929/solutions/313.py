class Node:

    def __init__(self):
        self.child = [None] * 26
        self.w = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Node()
        for w in words:
            p = self.root
            for ch in w[::-1]:
                k = ord(ch) - ord('a')
                if not p.child[k]:
                    p.child[k] = Node()
                p = p.child[k]
            p.w = True
        self.q = []

    def query(self, letter: str) -> bool:
        self.q.append(letter)
        p = self.root
        for i in range(len(self.q) - 1, -1, -1):
            k = ord(self.q[i]) - ord('a')
            if not p.child[k]:
                return False
            p = p.child[k]
            if p.w:
                return True
        return False

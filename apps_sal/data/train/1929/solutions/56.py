class Node:
    def __init__(self):
        self.c = collections.defaultdict(Node)
        self.e = 0


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Node()
        for w in words:
            temp = self.root
            for i in w:
                temp = temp.c[i]
            temp.e = 1
        self.w = []

    def query(self, letter: str) -> bool:
        self.w = [i.c[letter] for i in self.w + [self.root] if letter in i.c]
        return any(i.e for i in self.w)

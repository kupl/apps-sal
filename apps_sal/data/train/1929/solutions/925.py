from collections import deque


class Node:
    def __init__(self):
        self.child = dict()
        self.end = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Node()

        for i in words:
            self.insert(self.root, i[::-1])
        self.key = deque()

    def insert(self, root, key):
        for i in key:
            if root.child.get(i, None) == None:
                root.child[i] = Node()
            root = root.child[i]
        root.end = True

    def query(self, letter: str) -> bool:
        self.key.appendleft(letter)
        curr = self.root
        for i in self.key:
            if curr.child.get(i, None) == None:
                break
            curr = curr.child[i]
            if curr.end:
                return True
        return False

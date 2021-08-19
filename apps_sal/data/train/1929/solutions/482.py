class Node:

    def __init__(self, c):
        self.c = c
        self.childs = [None for i in range(26)]
        self.end = False


class Trie:

    def __init__(self):
        self.root = None
        self.p = []

    def insert(self, word):
        if self.root == None:
            self.root = Node('#')
        r = self.root
        for i in word[::-1]:
            if r.childs[ord(i) - 97] == None:
                r.childs[ord(i) - 97] = Node(i)
            r = r.childs[ord(i) - 97]
        r.end = True

    def search(self, word):
        if self.root == None:
            return False
        r = self.root
        for i in word[::-1]:
            if r.childs[ord(i) - 97] != None:
                r = r.childs[ord(i) - 97]
            else:
                return False
            if r.end:
                return True
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.tree = Trie()
        self.s = ''
        for word in words:
            self.tree.insert(word)

    def query(self, letter: str) -> bool:
        self.s += letter
        return self.tree.search(self.s)

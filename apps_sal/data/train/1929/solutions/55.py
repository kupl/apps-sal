def to_index(c):
    return ord(c) - ord('a')


class Node:
    def __init__(self, val=None):
        self.val = val
        self.end = False
        self.childs = [None] * (ord('z') - ord('a') + 1)


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        ptr = self.root
        for c in word:
            i = to_index(c)
            if ptr.childs[i] is None:
                node = Node(c)
                ptr.childs[i] = node
            ptr = ptr.childs[i]
        ptr.end = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for c in word:
            i = to_index(c)
            if ptr.childs[i] is None:
                return False
            ptr = ptr.childs[i]
        return ptr.end == True

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for c in prefix:
            i = to_index(c)
            if ptr.childs[i] is None:
                return False
            ptr = ptr.childs[i]
        return True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.t = Trie()
        for w in words:
            self.t.insert(w)
        self.d = set()
        self.n = 2000
        self.k = deque()
        self.store = {}

    def query(self, letter: str) -> bool:
        r = False
        if len(self.k) == self.n:
            self.k.popleft()
        i = to_index(letter)
        self.k.append(i)
        v = self.store.get(tuple(self.k), None)
        if v is not None:
            self.d, r = v
            return r
        new_d = set()
        for node in self.d:
            if node.childs[i] is not None:
                new_d.add(node.childs[i])
                if node.childs[i].end:
                    r = True
        if self.t.root.childs[i] is not None:
            new_d.add(self.t.root.childs[i])
            if self.t.root.childs[i].end:
                r = True
        self.d = tuple(new_d)
        self.store[tuple(self.k)] = (self.d, r)
        return r

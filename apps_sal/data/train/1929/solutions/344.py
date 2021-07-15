class node:
    def __init__(self):
        self.children = {}
        self.end = 0
        
class Trie:
    def __init__(self):
        self.root = node()
        
    def insert(self, w):
        r = self.root
        for l in w:
            r = r.children.setdefault(l, node())
        r.end = 1


class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.s = deque()
        for w in words: self.trie.insert(w[::-1])

    def query(self, letter: str) -> bool:
        self.s.appendleft(letter)
        cur = self.trie.root
        for c in self.s:
            if c in cur.children:
                cur = cur.children[c]
                if cur.end: return True 
            else: break
        return False


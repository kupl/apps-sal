class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        def insert(f):
            t = r
            for c in f:
                if c not in t.ch:
                    t.ch[c] = TrieNode()
                t = t.ch[c]
            t.ch['/'] = TrieNode()
            t = t.ch['/']
            t.d = True

        def search(f):
            t = r
            for c in f:
                t = t.ch[c]
                if t.d:
                    return False
            return True
        r = TrieNode()
        for f in folder:
            insert(f)
        l = []
        for f in folder:
            if search(f):
                l.append(f)
        return l


class TrieNode:
    def __init__(self):
        self.ch = {}
        self.d = False

class Solution:
    # 432 ms, 36.84%
    # def removeSubfolders(self, folder: List[str]) -> List[str]:
    #     folder.sort()
    #     l  = [folder[0]]
    #     p = folder[0]
    #     for f in folder[1:]:
    #         if not f.startswith(p + '/'):
    #             l.append(f)
    #             p = f
    #     return l
    
    
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

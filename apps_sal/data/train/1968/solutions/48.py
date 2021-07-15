class Trie:
    def __init__(self):
        self.sub = collections.defaultdict(Trie)
        self.index = -1
    
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Trie()
        for i in range(len(folder)):
            curr = root
            for c in folder[i]:
                curr = curr.sub[c]
            curr.index = i
        q, res = [root], []
        for t in q:
            if t.index >= 0:
                res.append(folder[t.index])
            for c in t.sub.keys():
                if c != '/' or t.index < 0:
                    q.append(t.sub.get(c))
        return res

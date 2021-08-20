class Trie:

    def __init__(self):
        self.sub = collections.defaultdict(Trie)
        self.index = -1


class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        self.root = Trie()
        for i in range(len(folder)):
            curr = self.root
            for ch in folder[i]:
                curr = curr.sub[ch]
            curr.index = i
        return self.bfs(self.root, folder)

    def bfs(self, node, folder):
        (q, ans) = ([node], [])
        for t in q:
            if t.index >= 0:
                ans.append(folder[t.index])
            for c in t.sub.keys():
                if c != '/' or t.index < 0:
                    q.append(t.sub.get(c))
        return ans

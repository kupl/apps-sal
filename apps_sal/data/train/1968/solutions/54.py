class Trie:

    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.index = -1


class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        self.root = Trie()
        for (i, f) in enumerate(folder):
            curr = self.root
            for ch in f:
                curr = curr.children[ch]
            curr.index = i
        return self.bfs(self.root, folder)

    def bfs(self, trie, folder):
        q = [trie]
        res = []
        for node in q:
            if node.index >= 0:
                res.append(folder[node.index])
            for c in node.children:
                if c != '/' or node.index == -1:
                    q.append(node.children.get(c))
        return res

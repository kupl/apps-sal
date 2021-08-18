class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['END'] = {}

    def search(self):

        def dfs(node, tmp, res):
            if 'END' in node:
                res.append(''.join(tmp))
            else:
                for ch in node:
                    tmp.append(ch)
                    dfs(node[ch], tmp, res)
                    tmp.pop()

        res, tmp = [], []
        dfs(self.root, tmp, res)
        return res


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        t = Trie()
        for f in folder:
            t.insert(f + '/')
        return [f[:-1] for f in t.search()]

        n = len(folder)

        folder = [f + '/' for f in folder]
        folder.sort()

        parent = 0
        for child in range(1, n):
            if folder[child].startswith(folder[parent]):
                folder[child] = None
            else:
                parent = child

        return [f[:-1] for f in folder if f is not None]

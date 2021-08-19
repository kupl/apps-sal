from collections import defaultdict


class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:

        def Trie():
            return defaultdict(Trie)
        trie = Trie()
        for f in folder:
            t = trie
            for c in f[1:].split('/'):
                t = t[c]
            t[None] = None
        res = []

        def dfs(t, path=[]):
            if None in t:
                res.append('/' + '/'.join(path))
                return
            for (c, nt) in list(t.items()):
                path.append(c)
                dfs(nt, path)
                path.pop()
        dfs(trie)
        return res

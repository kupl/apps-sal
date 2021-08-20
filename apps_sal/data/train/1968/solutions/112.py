class Trie:

    def __init__(self):
        self.child = {}
        self.isLast = False


class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        if not folder:
            return []
        root = Trie()
        for sf in folder:
            lists = sf[1:].split('/')
            if lists:
                self.add(root, lists)
        res = []
        self.dfs(root, [], res)
        return res

    def dfs(self, root, temp, res):
        cur = root
        if cur.isLast:
            res += ('/' + '/'.join(temp),)
            return
        for ch in cur.child:
            self.dfs(cur.child[ch], temp + [ch], res)

    def add(self, root, lists):
        cur = root
        for elem in lists:
            if elem not in cur.child:
                cur.child[elem] = Trie()
            cur = cur.child[elem]
        cur.isLast = True

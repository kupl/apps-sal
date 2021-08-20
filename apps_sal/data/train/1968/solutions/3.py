class Trie:

    def __init__(self):
        self.next = {}
        self.end_here = False


class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:

        def collect(curnode, res, curpath):
            if curnode.end_here:
                res.append('/'.join(curpath))
                return
            for folder in curnode.next:
                curpath.append(folder)
                collect(curnode.next[folder], res, curpath)
                curpath.pop()
        root = Trie()
        for f in folder:
            cur = root
            for seg in f.split('/'):
                if seg not in cur.next:
                    cur.next[seg] = Trie()
                cur = cur.next[seg]
            cur.end_here = True
        res = []
        collect(root, res, [])
        return res

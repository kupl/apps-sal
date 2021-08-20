class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:

        class Node:

            def __init__(self):
                self.is_path = False
                self.subs = {}

            def add_path(self, p, i=0):
                if i == len(p):
                    return
                n = p[i]
                if n not in self.subs:
                    self.subs[n] = Node()
                self.subs[n].is_path |= len(p) - i == 1
                self.subs[n].add_path(p, i + 1)
        t = Node()
        for f in folder:
            p = f.split('/')[1:]
            t.add_path(p)
        s = []
        p = []

        def dfs_visit(r, name=''):
            if r.is_path is True:
                s.append('/'.join(p) + '/' + name)
                return
            p.append(name)
            for (sub_name, sub) in r.subs.items():
                dfs_visit(sub, sub_name)
            p.pop()
        dfs_visit(t)
        return s

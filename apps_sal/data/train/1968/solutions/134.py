class Node:
    def __init__(self, name):
        self.name = name
        self.subdir = {}
        self.terminal = False

    def link(self, name, node):
        self.subdir[name] = node


class Solution:
    def dfs(self, node, dirstr, found):
        rtn = []
        if node.terminal and not found:
            rtn = [dirstr]
        for x in node.subdir.keys():
            rtn = rtn + self.dfs(node.subdir[x], dirstr + '/' + x, (found | node.terminal))
        return rtn

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Node('')
        for d in folder:
            seq = d.split('/')[1:]
            p = root
            for f in seq:
                if f not in p.subdir:
                    q = Node(f)
                    p.subdir[f] = q
                p = p.subdir[f]
            p.terminal = True
        return self.dfs(root, '', False)

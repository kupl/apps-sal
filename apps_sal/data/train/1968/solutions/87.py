class TreeNode:
    def __init__(self):
        self.val = '/'
        self.children = {}
        self.isleaf = False

    def insert(self, val):
        if not val:
            self.isleaf = True
            return
        if val[0] in self.children:
            self.children[val[0]].insert(val[1:])
            return
        newnode = TreeNode()
        newnode.val = val[0]
        self.children[val[0]] = newnode
        newnode.insert(val[1:])

    def isparent(self, val):
        if val and val[0] in self.children:
            return self.children[val[0]].isleaf or self.children[val[0]].isparent(val[1:])
        return False


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder = sorted(folder)
        ans = []

        fs = TreeNode()
        for f in folder:
            has_parent = fs.isparent(f.split('/'))
            if not has_parent:
                ans.append(f)
                fs.insert(f.split('/'))
        return ans

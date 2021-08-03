class TreeNode:
    def __init__(self):
        self.val = '/'
        self.children = []
        self.isleaf = False

    def insert(self, val):
        if not val:
            self.isleaf = True
            return
        for child in self.children:
            if child.val == val[0]:
                child.insert(val[1:])
                return
        newnode = TreeNode()
        newnode.val = val[0]
        self.children.append(newnode)
        newnode.insert(val[1:])

    def isparent(self, val):
        for child in self.children:
            if child.val == val[0]:
                if child.isleaf:
                    return True
                return child.isparent(val[1:])
        return False


def is_parent(f1, f2):
    f1 = f1.split('/')
    f2 = f2.split('/')
    if len(f1) > len(f2):
        return False
    return all([a == b for a, b in zip(f1, f2)])


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

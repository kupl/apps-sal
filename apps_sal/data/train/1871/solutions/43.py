class Solution:

    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.mx = 0
        path = []

        def getpath(root):
            if not root:
                return
            path.append(root.val)
            if len(path) > 1:
                self.mx = max(self.mx, abs(min(path[:-1]) - path[-1]))
                self.mx = max(self.mx, abs(max(path[:-1]) - path[-1]))
            getpath(root.left)
            getpath(root.right)
            path.pop()
        getpath(root)
        return self.mx

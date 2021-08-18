
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:

        self.mx = 0
        path = []

        def getpath(root):
            if not root:
                return
            path.append(root.val)
            self.mx = max(self.mx, abs(min(path) - max(path)))
            getpath(root.left)
            getpath(root.right)
            path.pop()

        getpath(root)
        return self.mx

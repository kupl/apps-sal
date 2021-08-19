class Solution:

    def minCameraCover(self, root):
        self.res = 0

        def dfs(root):
            if not root:
                return 2
            (l, r) = (dfs(root.left), dfs(root.right))
            if l == 0 or r == 0:
                self.res += 1
                return 1
            elif l == 1 or r == 1:
                return 2
            elif l == 2 or r == 2:
                return 0
        return (dfs(root) == 0) + self.res

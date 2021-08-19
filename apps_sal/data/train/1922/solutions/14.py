class Solution:

    def minCameraCover(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return 1
        self.ans = 0

        def dfs(t, pre=None):
            if t is None:
                return 0
            t.pre = pre
            dfs(t.left, t)
            dfs(t.right, t)
            if (not t.left or t.left.val < 0) and (not t.right or t.right.val < 0) and (t.val == 0):
                if pre and pre.val != -2:
                    pre.val = -2
                    self.ans += 1
                    if pre.pre:
                        pre.pre.val = -1
                if not pre and t.val == 0:
                    self.ans += 1
                    t.val = -1
        dfs(root)
        print(root)
        return self.ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # 1 means monitored, 2 means camera
        if root.left is None and root.right is None:
            return 1

        self.ans = 0
        # with dp?

        def dfs(t, pre=None):
            if t is None:
                return 0
            t.pre = pre
            # idea: put a camera above each leaf, mark around that we are ok, then cut those nodes from the tree
            # so that when we go up in the recursion there are new leaves
            dfs(t.left, t)
            dfs(t.right, t)

            if (not t.left or t.left.val < 0) and (not t.right or t.right.val < 0) and t.val == 0:
                if pre and pre.val != -2:
                    pre.val = -2
                    self.ans += 1
                    if pre.pre:
                        pre.pre.val = -1  # val of -1 means cut
                if not pre and t.val == 0:
                    self.ans += 1
                    t.val = -1

        dfs(root)
        print(root)
        return self.ans

        # min num of camera left

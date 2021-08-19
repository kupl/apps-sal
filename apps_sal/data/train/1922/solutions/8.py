# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        nothing = 0
        leaf = 1
        has = 2
        covered = 3
        coverme = 4
        self.ans = 0

        def rec(root):
            if not root:
                return 0
            if not root.left and not root.right:

                return leaf
            left = rec(root.left)
            right = rec(root.right)

            if left == leaf or right == leaf or left == coverme or right == coverme:
                self.ans += 1
                return has
            if left == has or right == has:
                return covered
            return coverme
        r = rec(root)
        if r == leaf or r == coverme:
            self.ans += 1
        return self.ans

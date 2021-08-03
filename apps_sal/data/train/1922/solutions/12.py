# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def solve(node):
            if node is None:
                return 0, 0, 1000
            l = solve(node.left)
            r = solve(node.right)

            dp0 = l[1] + r[1]
            dp1 = min(l[2] + min(r[1:]), min(l[1:]) + r[2])
            dp2 = 1 + min(l) + min(r)

            return dp0, dp1, dp2
        return min(solve(root)[1:])

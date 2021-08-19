# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def c(r, v):
            if not r:
                return 0
            mx = max(r.val, v)

            return (r.val >= mx) + c(r.left, mx) + c(r.right, mx)

        return c(root, root.val)

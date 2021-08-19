# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if root is None:
            return 0

        out = [0]
        #maxValue = -float('inf')

        def _recHelper(curr, maxValue):
            if curr is None:
                return

            if curr.val >= maxValue:
                out[0] += 1

            _recHelper(curr.left, max(curr.val, maxValue))
            _recHelper(curr.right, max(curr.val, maxValue))

        _recHelper(root, -float('inf'))

        return out[0]

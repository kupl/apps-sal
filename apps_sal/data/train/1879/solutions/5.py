# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        this_q = [root]
        result = 0

        while this_q:
            next_q = []
            temp = 0
            for node in this_q:
                temp += node.val
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)

            this_q = next_q
            result = max(0, temp)

        return result

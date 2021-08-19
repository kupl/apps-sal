# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def tranverse(node, ansestors, res):
            res = max(
                res,
                max([
                    abs(val - node.val)
                    for val in ansestors
                ]) if ansestors else 0,
            )
            ansestors.append(node.val)

            if node.left:
                res = tranverse(node.left, ansestors, res)

            if node.right:
                res = tranverse(node.right, ansestors, res)

            ansestors.pop()
            return res

        return tranverse(root, [], 0)

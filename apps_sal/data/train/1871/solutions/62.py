# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:

        def recAncestors(root, ancestors, dif):
            left_dif = 0
            right_dif = 0
            for node in ancestors:
                if dif < abs(root.val - node):
                    dif = abs(root.val - node)
            father = ancestors + [root.val]
            if root.left:
                left_dif = recAncestors(root.left, father, dif)
            if root.right:
                right_dif = recAncestors(root.right, father, dif)
            return max(left_dif, right_dif, dif)
        nodes = [root.val]
        right_wing, left_wing = 0, 0
        if root.right:
            right_wing = recAncestors(root.right, nodes, 0)
        if root.left:
            left_wing = recAncestors(root.left, nodes, 0)
        return max(right_wing, left_wing)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def util(root, maxDiff):
            if not root:
                return [], maxDiff
            lArr, maxDiff = util(root.left, maxDiff)
            rArr, maxDiff = util(root.right, maxDiff)
            
            for node in lArr:
                if abs(root.val - node.val) > maxDiff:
                    maxDiff = abs(root.val - node.val)
            for node in rArr:
                if abs(root.val - node.val) > maxDiff:
                    maxDiff = abs(root.val - node.val)
            return [root] + lArr + rArr, maxDiff
        arr, maxDiff = util(root, float('-inf'))
        return maxDiff

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # time O(n); space O(h)
        def match(original, copy):
            if not original:
                return None
            if original == target:
                return copy
            return match(original.left, copy.left) or match(original.right, copy.right)
        
        return match(original, cloned)

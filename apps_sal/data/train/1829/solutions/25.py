# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(n, maxval):
            if not n: return 0
            visible = 1 if n.val >= maxval else 0
            maxval = max(maxval, n.val)
            return traverse(n.left, maxval) + visible + traverse(n.right, maxval)
        
        return traverse(root, float(\"-inf\"))
            
            

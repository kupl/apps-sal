# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans = 0
        def traverse(node, max_v, min_v):
            self.ans = max( self.ans, abs(max_v- min_v) )
            _ = any(traverse(adj, max(max_v, adj.val), min(min_v, adj.val)) for adj in [node.left, node.right] if adj) 
        
        traverse(root, root.val, root.val)
        return self.ans


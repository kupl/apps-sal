# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def check(node, pathsum):
            if not node:
                return pathsum >= limit
            pathsum += node.val
            had_children = node.left or node.right
            if not check(node.left, pathsum):
                node.left = None
            if not check(node.right, pathsum):
                node.right = None
            return node.left or node.right if had_children else pathsum >= limit
        
        return root if check(root, 0) else None

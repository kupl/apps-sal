# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if root is None:
            return None
        
        print(root.val, limit)
        
        # If we have reached a root
        if root.left is None and root.right is None:
            if root.val < limit:
                return None
            else:
                return root
            
        left = self.sufficientSubset(root.left, limit - root.val)
        right = self.sufficientSubset(root.right, limit - root.val)
        
        if left is None and right is None:
            return None
        else:
            root.left = left
            root.right = right
            return root

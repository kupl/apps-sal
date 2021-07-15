# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        return 1 + self.helper(root.left, root.val) + self.helper(root.right, root.val)
    
    def helper(self, root: TreeNode, m: int) -> int:
        if root:
            if root.val >= m:
                return 1 + self.helper(root.left, max(root.val,m)) + self.helper(root.right, max(root.val,m))
            else:
                return self.helper(root.left, max(root.val,m)) + self.helper(root.right, max(root.val,m))
            
        else:
            return 0

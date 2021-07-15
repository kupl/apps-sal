# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def _goodNodes(self, root: TreeNode, maxSeen: int) -> int:
        print(f\"Node: {root.val}\")
        if not root:
            print(\"return 0\")
            return 0
        this = 1 if root.val >= maxSeen else 0
        left = 0
        right = 0
        if root.left:
            left = self._goodNodes(root.left, max(root.val, maxSeen))
        
        # right
        if root.right:
            right = self._goodNodes(root.right, max(root.val, maxSeen))
        
        return this + left + right
    
    def goodNodes(self, root: TreeNode) -> int:
        return self._goodNodes(root, root.val)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        maximum = -float(\"inf\")
        stack = []
        def dfs(root):
            nonlocal maximum
            if not root:
                maximum = max(abs(max(stack) - min(stack)), maximum)
                return
            stack.append(root.val)
            dfs(root.left)
            dfs(root.right)
            stack.pop()
        dfs(root)
        return maximum
            
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        
        self.mx=0
        def backtrack(root,curr,temp):
            
            if not root:
                return
            self.mx=max(self.mx,temp)
            if curr==\"left\":
                backtrack(root.right,\"right\",temp+1)
                backtrack(root.left,\"left\",1)
            else:
                backtrack(root.left,\"left\",temp+1)
                backtrack(root.right,\"right\",1)
            
        backtrack(root,\"left\",0)
        backtrack(root,\"right\",0)
        return self.mx

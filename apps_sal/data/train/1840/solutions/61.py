# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def traverse(node,d,curr):
            print((d,curr))
            if not node:
                res[0] = max(res[0],curr-1)
                return
            if d==0:
                traverse(node.left,0,1)
                traverse(node.right,1,curr+1)
            else:
                traverse(node.left,0,curr+1)
                traverse(node.right,1,1)
                
        if not root:
            return 0
        res = [-float('inf')]
        traverse(root.left,0,1)
        traverse(root.right,1,1)
        return res[0]
    
        


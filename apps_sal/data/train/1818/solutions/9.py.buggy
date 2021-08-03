# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        
        self.result = \"z\"*10000
        stack = []
        
        def traverse(node: TreeNode) -> str :
            if node:
                stack.append(chr(node.val + 97))
                if not node.left and not node.right:
                    self.result = min(self.result, \"\".join(reversed(stack)))                    
                traverse(node.left)
                traverse(node.right)
                stack.pop()                            
        
        traverse(root)
        return self.result
                    
            
        

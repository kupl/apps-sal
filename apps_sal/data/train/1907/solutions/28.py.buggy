# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def solve(node, value):
            \"\"\"recursively finds value in tree starting with parent node\"\"\"
            if not node:
                return None
            if node.val == value:
                return node
            left = solve(node.left, value)
            if left: 
                return left
            right = solve(node.right, value)
            if right:
                return right       
        
        return solve(cloned, target.val)
    
    
#             def solve(original,cloned,target):
#             if original == None:
#                 return None
#             if original == target:
#                 return cloned 
#             left = solve(original.left,cloned.left,target)
#             if left :
#                 return left 
#             right = solve(original.right, cloned.right,target)
#             if right :
#                 return right 
#         return solve(original,cloned,target)

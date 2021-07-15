# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        
        sums = []
        
        def addLevels(node, level):
            
            if level > len(sums):
                
                sums.append(0)
            
            sums[level - 1] += node.val
            
            if node.left != None:
                
                addLevels(node.left, level + 1)
            
            if node.right != None:
                
                addLevels(node.right, level + 1)
        
        if(root):
            
            addLevels(root, 1)
            return sums.index(max(sums)) + 1

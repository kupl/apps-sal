# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        stack = [root]
        ans = -1000000
        result = 1
        level = 1
        
        while stack:
            curr = 0
            newStack = []
            for x in stack:
                curr += x.val
                if x.left:
                    newStack.append(x.left)
                if x.right: 
                    newStack.append(x.right)
            
            stack = newStack
            
            if curr > ans:
                ans = curr
                result = level
                
            level += 1
            
        return result

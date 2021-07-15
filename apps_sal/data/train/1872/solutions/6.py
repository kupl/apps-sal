# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [root]
        levelsum = 0
        maxlevel = float('-inf')
        maxsum = float('-inf')
        currentlevel = 0
        
        while stack:
            slen = len(stack)
            currentlevel += 1
            while slen > 0:
                node = stack.pop(0)
                levelsum += node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                slen -=1
            
            if levelsum > maxsum:
                maxlevel = currentlevel
                maxsum = levelsum
            
            levelsum = 0
        
        return maxlevel

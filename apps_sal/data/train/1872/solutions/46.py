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
        
        queue = [root]
        maxSum = root.val
        res = 1
        level = 0
        
        while queue:
            size = len(queue)
            currSum = 0
            level += 1
            
            for _ in range(size):
                node = queue.pop(0)
                currSum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if maxSum < currSum:
                maxSum = currSum
                res = level
                
        return res 

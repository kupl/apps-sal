# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root: return 0
        
        levels = []
        
        queue = [root]
        
        while queue:
            new_queue = []
            
            ttl = 0
            for node in queue:
                ttl += node.val
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            levels.append(ttl)
            queue = new_queue
        
        curr_max = -float('inf')
        curr_index = -1
        for i, num in enumerate(levels):
            if num > curr_max:
                curr_index = i
                curr_max = num
        return curr_index+1
                
        
        


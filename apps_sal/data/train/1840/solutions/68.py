# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        
        levels = [root]
        ret = 0
        dp_r = defaultdict(int)
        dp_l = defaultdict(int)
        while levels:
            
            nxt = []
            
            for p in levels:
                if p.left:
                    nxt.append(p.left)
                    dp_l[p.left] = dp_r[p] + 1 
                    ret = max(ret, dp_l[p.left])
                    
                if p.right:
                    nxt.append(p.right)
                    dp_r[p.right] = dp_l[p] + 1 
                    ret = max(ret, dp_r[p.right])
            
            levels = nxt
            
            
        return ret

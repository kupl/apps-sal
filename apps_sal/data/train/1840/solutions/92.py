# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def run(self, node, side, count, memo):
        if not node:
            return count
        
        if node in memo:
            if memo[node][side] > -1:
                return memo[node][side]
        
        memo[node] = [-1, -1, -1]
        
        if side == 0:
            result = self.run(node.right, 1, count+1, memo)
        elif side == 1:
            result = self.run(node.left, 0, count+1, memo)
        else:
            using = max(self.run(node.right, 1, 1, memo), self.run(node.left, 0, 1, memo))
            notUsing = max(self.run(node.right, -1, 0, memo), self.run(node.left, -1, 0, memo))
            result = max(using, notUsing)
        
        memo[node][side] = result
        
        return result
        
    
    def longestZigZag(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return self.run(root, -1, 0, {})-1

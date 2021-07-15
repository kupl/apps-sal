# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, 0, float('-inf'))
    
    def dfs(self, root, good, max_val): 
        if root == None: 
            return good 
        if root.val >= max_val: 
            good += 1 
            max_val = root.val 
        good = self.dfs(root.left, good, max_val)
        good = self.dfs(root.right, good, max_val)
        return good
        


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        # initialize a difference variable for the difference value
        # have to account for if max is a negative number. 0 is > -num
        self.max_diff = -float(\"inf\")
        # call helper function passing in the root (where you start) and an empty list [] (holds the path of travel)
        self.dfs(root, [])
        
        # return out the max difference value
        return self.max_diff
    
    # helper method to track path and perform subtraction
    def dfs(self, root, path):
        # if there is not root
        if not root:
            # print(\"PATH: \", path)
            self.max_diff = max(self.max_diff, max(path) - min(path))
            return
        self.dfs(root.left, path + [root.val])
        self.dfs(root.right, path + [root.val])
        

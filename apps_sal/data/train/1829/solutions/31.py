# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
       
        self.count = 0
        self.dfs(root, root.val)
        return self.count
    def dfs(self, root, max_num):
        if root is None:
            return
        if root.val >= max_num:
            max_num = root.val
            self.count += 1
        self.dfs(root.left, max_num)
        self.dfs(root.right, max_num)

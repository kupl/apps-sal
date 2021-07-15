# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_cnt=0
    
    def longestZigZag(self, root: TreeNode) -> int:
        self.dfs(root,True,0)
        self.dfs(root,False,0)
        return self.max_cnt
        
    def dfs(self, root, isLeft, cnt):
        if root is None:
            return
        self.max_cnt=max(self.max_cnt,cnt)
        if isLeft:
            self.dfs(root.left,False,cnt+1)
            self.dfs(root.right,True,1)
        else:
            self.dfs(root.right,True,cnt+1)
            self.dfs(root.left,False,1)

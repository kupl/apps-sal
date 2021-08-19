# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.ans = None
        self.num = target.val
        self.dfs(cloned)
        return self.ans

    def dfs(self, curr):
        if(curr is None):
            return
        if(curr.val == self.num):
            self.ans = curr
            return
        self.dfs(curr.left)
        self.dfs(curr.right)

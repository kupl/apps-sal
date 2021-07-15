# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node):
            if node:
                yield node
                yield from dfs(node.left)
                yield from dfs(node.right)
        
        for it1, it2 in zip(dfs(original), dfs(cloned)):
            if it1 == target:
                return it2
        
        return -1

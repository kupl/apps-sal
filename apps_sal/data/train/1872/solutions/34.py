# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        dic = collections.defaultdict(int)
        
        def dfs(node, level):
            if not node:
                return
            else:
                dic[level] += node.val
            dfs(node.left, level+1)
            dfs(node.right, level+1)
            
        dfs(root,1)
        
        res = 1
        Max = float('-inf')
        for level,value in list(dic.items()):
            if value>Max:
                Max = value
                res = level
        return res


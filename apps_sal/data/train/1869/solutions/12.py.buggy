# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import re

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        vals = [(len(s[1]), int(s[2])) for s in re.findall(\"((-*)(\\d+))\", S)][::-1]

        def dfs(level):
            if not vals or level != vals[-1][0]:
                return None

            node = TreeNode(vals.pop()[1])
            node.left = dfs(level + 1)
            node.right = dfs(level + 1)
            return node

        return dfs(0)
        

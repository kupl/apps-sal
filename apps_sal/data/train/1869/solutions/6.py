# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, s: str) -> TreeNode:
        self.index = 0
        def dfs(depth):
            if self.index == len(s):
                return
            for i in range(depth):
                if s[self.index+i] != '-':
                    return
            self.index += depth
            curr = 0
            while self.index < len(s) and s[self.index].isdigit():
                curr = curr * 10 + int(s[self.index])
                self.index += 1
            node = TreeNode(curr)
            node.left = dfs(depth+1)
            node.right = dfs(depth+1)
            return node
        return dfs(0)
    


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        def helper(depth):
            if depth != self.expected_depth:
                return None
            if self.i == len(S):
                return None
            n = 0
            while self.i < len(S) and S[self.i] != \"-\":
                n = n * 10 + int(S[self.i])
                self.i += 1
            self.expected_depth = 0
            while self.i < len(S) and S[self.i] == \"-\":
                self.expected_depth += 1
                self.i += 1
            node = TreeNode(n)
            node.left = helper(depth + 1)
            node.right = helper(depth + 1)
            return node
        
        self.i = 0
        self.expected_depth = 0
        return helper(0)

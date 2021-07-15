# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
# recursive
# use a direction to mark curr direction
# if dir is right: call 1+ helper(root.left, left)
        self.longest = 0
        def dfs(node, dirc):
            if not node:return 0
            left = dfs(node.left, \"left\")
            right = dfs(node.right, \"right\")
            self.longest = max(self.longest, left, right)
            if dirc == \"right\":
                return 1 + left
            else:
                return 1 + right

        dfs(root,\"left\")
        return self.longest

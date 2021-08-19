# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        cnt = 0

        def dfs(node):
            nonlocal cnt
            res.append(node.val)
            if res[-1] == max(res):
                cnt += 1
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            if res:
                res.pop()
        dfs(root)
        return cnt

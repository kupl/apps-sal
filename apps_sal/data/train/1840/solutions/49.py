# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:

        memo = {}

        ans = [0]

        def cur(node: TreeNode):
            if node in list(memo.keys()):
                return

            if node != None:
                memo[node] = [0, 0]
            if node.left != None:
                cur(node.left)
                memo[node][0] = memo[node.left][1] + 1
                ans[0] = max(ans[0], memo[node][0])
            if node.right != None:
                cur(node.right)
                memo[node][1] = memo[node.right][0] + 1
                ans[0] = max(ans[0], memo[node][1])

        cur(root)

        return ans[0]

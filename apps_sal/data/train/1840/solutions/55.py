# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        dp = [0]

        def f(n, ind):
            if not n:
                dp[ind] = (0, 0)
            else:
                dp.extend([0, 0])
                temp = len(dp)
                f(n.left, temp - 2)
                f(n.right, temp - 1)
                dp[ind] = (dp[temp - 1][1] + 1, dp[temp - 2][0] + 1)
        f(root, 0)
        m = -1
        # print(dp)
        for i in dp:
            m = max(i[0], i[1], m)
        return m - 1

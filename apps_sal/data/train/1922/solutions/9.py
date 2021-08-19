# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # self.times = 0
        self.DP = dict()

        def dp(node, flag):
            if (node, flag) in self.DP:
                return self.DP[(node, flag)]
            # self.times += 1
            # print(self.times)
            if flag == 0 and node is None:
                result = 1
            elif node is None:
                result = 0
            elif flag == 2:  # satisfied
                result = min(dp(node.left, 1) + dp(node.right, 1), dp(node.left, 2) + dp(node.right, 2) + 1)
            elif flag == 1:  # self or descend should be
                a = dp(node.left, 0)
                b = dp(node.right, 1)
                aa = dp(node.left, 1)
                bb = dp(node.right, 0)
                result = min(a + b, aa + bb, a + bb, dp(node.left, 2) + dp(node.right, 2) + 1)
            else:
                result = dp(node.left, 2) + dp(node.right, 2) + 1
            self.DP[(node, flag)] = result
            return result
        return min(dp(root, 0), dp(root, 1))

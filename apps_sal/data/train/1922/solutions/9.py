
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.DP = dict()

        def dp(node, flag):
            if (node, flag) in self.DP:
                return self.DP[(node, flag)]
            if flag == 0 and node is None:
                result = 1
            elif node is None:
                result = 0
            elif flag == 2:
                result = min(dp(node.left, 1) + dp(node.right, 1), dp(node.left, 2) + dp(node.right, 2) + 1)
            elif flag == 1:
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

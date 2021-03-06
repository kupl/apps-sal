class Solution:

    def minCameraCover(self, root: TreeNode) -> int:

        def dp(node):
            if not node:
                return [0, 0, float(inf)]
            L = dp(node.left)
            R = dp(node.right)
            dp0 = L[1] + R[1]
            dp1 = min(L[2] + min(R[1:]), min(L[1:]) + R[2])
            dp2 = 1 + min(L) + min(R)
            return [dp0, dp1, dp2]
        return min(dp(root)[1:])

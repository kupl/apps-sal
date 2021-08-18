class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        if not root:
            return 0

        def solve(node):
            if not node:
                return 0, 0, float('inf')
            L = solve(node.left)
            R = solve(node.right)

            dp0 = L[1] + R[1]

            dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
            dp2 = 1 + min(L) + min(R)

            return dp0, dp1, dp2
        print(solve(root))
        return min(solve(root)[1:])

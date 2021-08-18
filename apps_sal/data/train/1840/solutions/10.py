class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        ans = [-1]

        def aux(root, isleft, ans):
            if not root:
                return -1
            left = aux(root.left, 1, ans) + 1
            right = aux(root.right, 0, ans) + 1
            ans[0] = max(ans[0], left, right)
            if isleft:
                return right
            else:
                return left

        if not root:
            return 0
        aux(root, 0, ans)
        return ans[0]

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        c = [0, 0]

        def count(root):
            if not root:
                return 0
            l, r = count(root.left), count(root.right)
            if root.val == x:
                c[0], c[1] = l, r

            return l + r + 1
        return count(root) / 2 < max(max(c), n - sum(c) - 1)

class Solution:
    def __init__(self):
        self.lcnt, self.rcnt = 0, 0

    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:

        rootCnt = self.dfs(root, x)

        return max([rootCnt - self.lcnt - self.rcnt - 1, self.lcnt, self.rcnt]) > n / 2

    def dfs(self, node: TreeNode, x: int) -> int:
        if not node:
            return 0
        left = self.dfs(node.left, x)
        right = self.dfs(node.right, x)

        if node.val == x:
            self.lcnt = left
            self.rcnt = right

        return 1 + left + right

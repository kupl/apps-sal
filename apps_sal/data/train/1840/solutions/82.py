class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.sol = 0
        left = self.DFS(root, 0)
        right = self.DFS(root, 1)

        return self.sol - 1

    def DFS(self, node, direction):
        if not node:
            return 0
        left = self.DFS(node.left, 0)
        right = self.DFS(node.right, 1)
        self.sol = max(left + 1, right + 1, self.sol)
        print((self.sol))
        if direction == 0:
            return right + 1
        else:
            return left + 1

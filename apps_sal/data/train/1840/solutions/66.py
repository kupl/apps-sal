class Solution:

    def longestZigZag(self, root: TreeNode) -> int:
        self.mx = 0
        out = self.traverse(root, 0)
        out = self.traverse(root, 1)
        return self.mx - 1

    def traverse(self, node, ctype):
        if node is None:
            return (0, 0)
        ll = lr = rl = rr = 0
        if node.left:
            (ll, lr) = self.traverse(node.left, 0)
        if node.right:
            (rl, rr) = self.traverse(node.right, 1)
        best = max(lr, rl) + 1
        self.mx = max(self.mx, best)
        return (1 + lr, 1 + rl)

class Solution:
    ans = 0

    def maxAncestorDiff(self, root: TreeNode) -> int:

        def visit(root, ancs):
            if root is None:
                return
            if ancs:
                self.ans = max(self.ans, max((abs(root.val - o) for o in ancs)))
            visit(root.left, ancs + [root.val])
            visit(root.right, ancs + [root.val])
        visit(root, [])
        return self.ans

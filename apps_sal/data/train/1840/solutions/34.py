class Solution:
    def longestZigZagRec(self, root, goLeft, steps):
        if root == None:
            return steps - 1
        if goLeft:
            return max(
                self.longestZigZagRec(root.left, False, steps + 1),
                self.longestZigZagRec(root.right, True, 1)
            )

        else:
            return max(
                self.longestZigZagRec(root.right, True, steps + 1),
                self.longestZigZagRec(root.left, False, 1)
            )

    def longestZigZag(self, root: TreeNode) -> int:
        if root == None:
            return 0

        return max(
            self.longestZigZagRec(root, True, 0),
            self.longestZigZagRec(root, False, 0)
        )

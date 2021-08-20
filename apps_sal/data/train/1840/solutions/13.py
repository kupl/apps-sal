class Solution:

    def longestZigZag(self, root: TreeNode) -> int:
        if root == None:
            return 0
        maxZigZag = 0

        def zigZagStart(root):
            nonlocal maxZigZag
            if root == None or (root.left == None and root.right == None):
                return [0, 0]
            (ll, lr) = zigZagStart(root.left)
            (rl, rr) = zigZagStart(root.right)
            bestLeft = 0
            bestRight = 0
            if root.left:
                bestLeft = 1 + lr
            if root.right:
                bestRight = 1 + rl
            maxZigZag = max(maxZigZag, bestLeft, bestRight)
            return [bestLeft, bestRight]
        zigZagStart(root)
        return maxZigZag

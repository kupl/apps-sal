class Solution:
    def longestZigZag(self, root: TreeNode) -> int:

        seenSoFar = 0

        def longestZigZagUtil(root):
            nonlocal seenSoFar
            if not root:
                return 0, 0

            Ll, Lr = longestZigZagUtil(root.left)
            Rl, Rr = longestZigZagUtil(root.right)

            curL, curR = 0, 0
            if root.left:
                curL = 1 + Lr
                seenSoFar = max(seenSoFar, Ll)
            if root.right:
                curR = 1 + Rl
                seenSoFar = max(seenSoFar, Rr)

            return curL, curR

        l, r = longestZigZagUtil(root)
        return max(l, r, seenSoFar)

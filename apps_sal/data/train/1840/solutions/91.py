class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def zigzag(node, mz):
            if not node:
                return -1, -1
            l1, r1 = zigzag(node.left, mz)
            l2, r2 = zigzag(node.right, mz)
            mz[0] = max(mz[0], r1 + 1, l2 + 1)
            return r1 + 1, l2 + 1

        maxzigzag = [0]
        zigzag(root, maxzigzag)
        zigzag(root, maxzigzag)

        return maxzigzag[0]

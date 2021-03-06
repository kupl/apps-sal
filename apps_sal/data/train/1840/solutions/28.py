class Solution:

    def longestZigZag(self, root: TreeNode) -> int:

        def zigzag(node, left, acum):
            if node is None:
                return acum - 1
            if left:
                return max(zigzag(node.left, False, acum + 1), zigzag(node.left, True, 0))
            else:
                return max(zigzag(node.right, True, acum + 1), zigzag(node.right, False, 0))
        return max(zigzag(root, True, 0), zigzag(root, False, 0))

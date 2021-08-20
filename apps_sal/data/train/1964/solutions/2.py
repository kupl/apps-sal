class Solution:

    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """

        def depth(node):
            if node is None:
                return 0
            return 1 + max(depth(node.left), depth(node.right))
        d = depth(root)
        result = [[''] * (2 ** d - 1) for _ in range(d)]

        def helper(row, startcol, endcol, node):
            if node is None:
                return
            col = (startcol + endcol) // 2
            result[row][col] = str(node.val)
            helper(row + 1, startcol, col - 1, node.left)
            helper(row + 1, col + 1, endcol, node.right)
        helper(0, 0, 2 ** d - 2, root)
        return result

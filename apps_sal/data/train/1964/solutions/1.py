class Solution:

    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """

        def depth(root):
            if root is None:
                return 0
            return max(depth(root.left), depth(root.right)) + 1

        def printT(x, root, dep):
            if root is not None:
                ans[n - dep - 1][x] = str(root.val)
                printT(x - 2 ** (dep - 1), root.left, dep - 1)
                printT(x + 2 ** (dep - 1), root.right, dep - 1)
        n = depth(root)
        m = 2 ** n - 1
        ans = [[''] * m for __ in range(n)]
        printT((m - 1) // 2, root, n - 1)
        return ans

class Solution:

    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root:
            return ['']

        def getDepth(root):
            if not root:
                return 0
            return 1 + max(getDepth(root.left), getDepth(root.right))
        d = getDepth(root)
        cols = 2 ** d - 1
        result = [['' for i in range(cols)] for j in range(d)]

        def helper(root, d, pos):
            result[-d - 1][pos] = str(root.val)
            if root.left:
                helper(root.left, d - 1, pos - 2 ** (d - 1))
            if root.right:
                helper(root.right, d - 1, pos + 2 ** (d - 1))
        helper(root, d - 1, 2 ** (d - 1) - 1)
        return result

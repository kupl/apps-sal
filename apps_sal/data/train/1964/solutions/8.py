class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def h(node):
            if not node:
                return 0
            return 1 + max(h(node.left), h(node.right))

        height = h(root)
        m = height
        n = 2**height - 1
        ret = [['' for _ in range(n)] for __ in range(m)]

        def put(node, i, l, r):
            mid = (l + r) // 2
            ret[i][mid] = str(node.val)
            if node.left:
                put(node.left, i + 1, l, mid - 1)
            if node.right:
                put(node.right, i + 1, mid + 1, r)

        put(root, 0, 0, n - 1)
        return ret

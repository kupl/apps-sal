class Solution:

    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """

        def depth(node):
            if not node:
                return 0
            return 1 + max(depth(node.left), depth(node.right))
        dep = depth(root)
        wid = 2 ** dep - 1
        frame = [['' for j in range(wid)] for i in range(dep)]

        def filler(node, level, low, high):
            if not node or low > high:
                return
            mid = (low + high) // 2
            frame[level][mid] = str(node.val)
            filler(node.left, level + 1, low, mid)
            filler(node.right, level + 1, mid + 1, high)
        filler(root, 0, 0, wid)
        return frame

class Solution:

    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        height = 0

        def Dfs(node, currHeight):
            nonlocal height
            if node == None:
                height = max(currHeight - 1, height)
                return
            Dfs(node.left, currHeight + 1)
            Dfs(node.right, currHeight + 1)
        Dfs(root, 1)
        ret = [[''] * (2 ** height - 1) for _ in range(height)]

        def rec(node, currHeight, start, end):
            if node == None:
                return
            center = int((start + end) / 2)
            ret[currHeight][center] = str(node.val)
            rec(node.left, currHeight + 1, start, center - 1)
            rec(node.right, currHeight + 1, center + 1, end)
        rec(root, 0, 0, 2 ** height - 1)
        return ret

class Solution:

    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        level = [root]
        tree = []
        while any(level):
            tree.append([str(node.val) if node else '' for node in level])
            level = [leaf for node in level for leaf in ((node.left, node.right) if node else (None, None))]
        ans = [['' for _ in range(2 ** len(tree) - 1)] for _ in range(len(tree))]
        for r in range(len(tree)):
            i = -2 ** (len(tree) - r - 1) - 1
            for c in tree[r]:
                i += 2 ** (len(tree) - r)
                ans[r][i] = c
        return ans

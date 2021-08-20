class Solution:

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.dfs(root)[2]

    def dfs(self, node):
        """return [min, max, is_BST]"""
        if node is None:
            return [None, None, True]
        L = self.dfs(node.left)
        R = self.dfs(node.right)
        if not L[2] or not R[2] or (L[1] is not None and L[1] >= node.val) or (R[0] is not None and R[0] <= node.val):
            return [None, None, False]
        if L[0] is not None:
            min = L[0]
        else:
            min = node.val
        if R[1] is not None:
            max = R[1]
        else:
            max = node.val
        return [min, max, True]

class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root:
            return
        if d == 1:
            new = TreeNode(v)
            new.left = root
            return new
        if d == 2:
            right, left = TreeNode(v), TreeNode(v)

            right.right = root.right
            left.left = root.left

            root.right, root.left = right, left
        else:
            self.addOneRow(root.right, v, d - 1)
            self.addOneRow(root.left, v, d - 1)
        return root

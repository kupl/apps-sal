class Solution:
    def __init__(self):
        self.data_dict = dict()

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        if root in self.data_dict:
            return self.data_dict[root]

        if not root.left and not root.right:
            self.data_dict[root] = root.val
            return root.val

        res = 0

        if root.left:
            res += self.rob(root.left.left) + self.rob(root.left.right)

        if root.right:
            res += self.rob(root.right.left) + self.rob(root.right.right)

        res = max(self.rob(root.left) + self.rob(root.right), res + root.val)
        self.data_dict[root] = res

        return res

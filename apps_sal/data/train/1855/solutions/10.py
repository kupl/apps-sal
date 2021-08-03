class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        return self.inorder(root, res)

    def inorder(self, root, res):
        if not root:
            return True
        if self.inorder(root.left, res) == False:
            return False
        if len(res) != 0:
            last = res.pop()
            if last >= root.val:
                return False
            res.append(last)
        res.append(root.val)
        if self.inorder(root.right, res) == False:
            return False
        return True

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxHeight = 0
        self.leftNode = None
        self.findNode(root, 1)
        return self.leftNode

    def findNode(self, root, height):
        if not root:
            return
        if height > self.maxHeight:
            self.leftNode = root.val
            self.maxHeight = height
        self.findNode(root.left, height + 1)
        self.findNode(root.right, height + 1)

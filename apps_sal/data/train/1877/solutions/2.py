class Solution:

    def sumofnodes(self, root, cursum):
        if root is None:
            return 0
        cursum += root.val
        self.sumdict[root] = cursum
        self.sumofnodes(root.left, cursum)
        self.sumofnodes(root.right, cursum)

    def maxpathsum(self, root):
        if root.left == None and root.right == None:
            self.maxdict[root] = self.sumdict[root]
        elif root.left and root.right:
            self.maxdict[root] = max(self.maxpathsum(root.left), self.maxpathsum(root.right))
        elif root.right:
            self.maxdict[root] = self.maxpathsum(root.right)
        else:
            self.maxdict[root] = self.maxpathsum(root.left)
        return self.maxdict[root]

    def deletenodes(self, root, limit):
        if root is None:
            return
        if root.left and self.maxdict[root.left] < limit:
            root.left = None
        if root.right and self.maxdict[root.right] < limit:
            root.right = None
        self.deletenodes(root.left, limit)
        self.deletenodes(root.right, limit)

    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        self.sumdict = {}
        self.sumofnodes(root, 0)
        self.maxdict = {}
        self.maxpathsum(root)
        self.deletenodes(root, limit)
        if self.maxdict[root] < limit:
            return None
        else:
            return root

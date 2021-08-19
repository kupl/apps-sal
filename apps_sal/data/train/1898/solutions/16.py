class Solution:

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.deletes = set(to_delete)
        self.res = list()
        root = self.helper(root)
        if root:
            self.res.append(root)
        return self.res

    def helper(self, root):
        if not root:
            return root
        root.left = self.helper(root.left)
        root.right = self.helper(root.right)
        if root.val in self.deletes:
            if root.left:
                self.res.append(root.left)
            if root.right:
                self.res.append(root.right)
            root = None
        return root

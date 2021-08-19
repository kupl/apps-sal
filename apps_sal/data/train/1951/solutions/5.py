class Solution:

    def findTree(self, root, node):
        if not root:
            return node
        if node.val > root.val:
            node.left = root
            return node
        root.right = self.findTree(root.right, node)
        return root

    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        return self.findTree(root, TreeNode(val))

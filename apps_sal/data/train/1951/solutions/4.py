class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        node = TreeNode(val)
        if not root:
            return node
        if val > root.val:
            node.left = root
            return node
        right = self.insertIntoMaxTree(root.right, val)
        root.right = right
        return root

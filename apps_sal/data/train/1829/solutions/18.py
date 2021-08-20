class Solution:

    def traverse(self, node, max_val):
        if node.val >= max_val:
            self.traverse_count += 1
        max_val = max(max_val, node.val)
        if node.left:
            self.traverse(node.left, max_val)
        if node.right:
            self.traverse(node.right, max_val)

    def goodNodes(self, root: TreeNode) -> int:
        if root:
            self.traverse_count = 0
            self.traverse(root, float('-inf'))
            return self.traverse_count
        return 0
